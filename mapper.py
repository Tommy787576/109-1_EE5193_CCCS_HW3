#!/usr/bin/env python

import sys

dic = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, \
    'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    word = words[3].split(':')

    date = word[0][1:].split('/')
    time = word[1]

    value = 1
    key = date[2] + '-' + str(dic[date[1]]) + '-' + date[0] + \
        ' T ' + time + ':00:00.000'
    print("%s\t%d" %(key, value))
