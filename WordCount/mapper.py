#!/opt/anaconda3/envs/project/bin/python

import re
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print("%s\t%s" % (re.compile("[^a-z^A-Z]").sub("", word).lower(), 1))