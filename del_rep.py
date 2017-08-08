#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            sample = ','.join(list(set(i.split('\t')[2].split(','))))
            tools = ','.join(list(set(i.split('\t')[3].split(','))))
            total = i.strip().split('\t')
            total[2] = sample
            total[3] = tools
            print('\t'.join(total))


if __name__ == '__main__':
    main(sys.argv[1])
