#!/usr/bin/env python3

import sys
from string import ascii_uppercase, ascii_lowercase, digits

MAX_PATTERN_LENGTH = 20280

class MaxLengthException(Exception):
    pass

class WasNotFoundException(Exception):
    pass


def pattern_gen(length):
    """
    Generate a pattern of a given length up to a maximum
    of 20280 - after this the pattern would repeat
    """
    if length >= MAX_PATTERN_LENGTH:
        raise MaxLengthException('ERROR: Pattern length exceeds '
                                 'maximum of {0}'.format(MAX_PATTERN_LENGTH))

    pattern = ''
    for upper in ascii_uppercase:
        for lower in ascii_lowercase:
            for digit in digits:
                if len(pattern) < length:
                    pattern += upper+lower+digit
                else:
                    out = pattern[:length]
                    return out


def pattern_search(search_pattern):
    """
    Search for search_pattern in pattern. Convert from hex if needed
    Looking for needle in haystack
    """
    needle = search_pattern

    try:
        if needle.startswith('0x'):
            # Strip off '0x', convert to ASCII and reverse
            needle = needle[2:]
            needle = bytearray.fromhex(needle).decode('ascii')
            needle = needle[::-1]
    except (ValueError, TypeError) as e:
        raise

    haystack = ''
    for upper in ascii_uppercase:
        for lower in ascii_lowercase:
            for digit in digits:
                haystack += upper+lower+digit
                found_at = haystack.find(needle)
                if found_at > -1:
                    return found_at

    raise WasNotFoundException('Couldn`t find {0} ({1}) '
                               'anywhere in the pattern.'.format(search_pattern,
                                                                 needle))


def print_help():
    print('Usage: {0} [LENGTH|PATTERN]\n'.format(sys.argv[0]))
    print('Generate a pattern of length LENGTH or search for PATTERN and ')
    print('return its position in the pattern.\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        sys.exit(0)

    if sys.argv[1].isdigit():
        try:
            pat = pattern_gen(int(sys.argv[1]))
            print(pat)
        except MaxLengthException as e:
            print(e)
    else:
        try:
            found = pattern_search(sys.argv[1])
            print('Pattern {0} first occurrence at '
                  'position {1} in pattern.'.format(sys.argv[1], found))
        except WasNotFoundException as e:
            print(e)
            sys.exit(1)
        except (ValueError, TypeError):
            print('Unable to convert hex input for searching. Invalid hex?')
            sys.exit(1)

