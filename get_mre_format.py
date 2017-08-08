#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-06-20 20:02:40
import sys

'''
python get_mre_format.py 2_input.merge > mre_format
'''

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            total = i.strip().split('\t')
            del total[9]
            print '\t'.join(total)


if __name__ == '__main__':
    main(sys.argv[1])
