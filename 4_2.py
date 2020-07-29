#!/usr/bin/env python3

import collections
import string
import sys
import io

def swap(t):
	return t[1], t[0]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with io.open(filename, encoding=('utf-8')) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
wordsp = words.items()
for tup in sorted(wordsp, key=swap):
    print("'{0}' occurs {1} times".format(tup[0], tup[1]))