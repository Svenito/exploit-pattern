# Python Exploit Pattern Tool

Python implementation of Metasploit's pattern generator and search. Should be python version agnostic, tested and working with Python 2.7.12 up to and including Python 3.7.5.

Starts faster and rolls both tools into one.

No extra dependencies required, works with vanilla python

## Generate a pattern

    $> pattern.py 100
    Aa0Aa0Aa1Aa1Aa2Aa2Aa3Aa3Aa4Aa4Aa5Aa5Aa6Aa6Aa7Aa7Aa8Aa8Aa9Aa9Ab0Ab0Ab1Ab1Ab2Ab2Ab3Ab3Ab4Ab4Ab5Ab5Ab6A

## Search for a pattern

    $> pattern.py Bf4B
    Pattern Bf4 first occurrence at position 942 in pattern.
    $> pattern.py 0x42346642
    Pattern 0x42346642 first occurrence at position 942 in pattern.

## Use it in your own python code

After placing pattern.py in the same directory as your script:

```python
from pattern import pattern_gen

print(pattern_gen(10))
```

or

```python
from pattern import pattern_search

found_at = pattern_search('Bf4B')
```

## Obtaining

Clone the repo, or if you are on a machine without git you can use

    $> curl https://is.gd/xpattern -o pattern.py

or

    $> wget https://is.gd/xpattern -o pattern.py

Or change the `pattern.py` to whatever filename you like

## License

The MIT License (MIT)
Copyright (c) 2014 Sven Steinbauer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
