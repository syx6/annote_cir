#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
For unique circRNAs
python unique.py ccRCC.cir > uniq.cir
'''


import sys
from collections import defaultdict


def main(file1):
    a = defaultdict(list)
    b = defaultdict(list)
    c = defaultdict(list)
    d = {}
    with open(file1, 'r') as f1:
        for i in f1:
            cir = i.split('\t')[0]
            junc = i.split('\t')[1]
            sample = i.split('\t')[2]
            tool = i.split('\t')[3]
            strand = i.strip().split('\t')[-1]
            a[cir].append(junc)
            b[cir].append(sample)
            c[cir].append(tool)
            d[cir] = strand
    for i in a:
        print(i + '\t' + ','.join(a[i]) + '\t' + ','.join(b[i]) + '\t' + ','.join(c[i]) + '\t' + d[i])


if __name__ == '__main__':
    main(sys.argv[1])
