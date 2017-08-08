#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-06-28 14:57:18
import sys

def main(file1, file2):
    a = {}
    with open(file1, 'r') as f1:
        for i in f1:
            gene = i.split('\t')[0]
            mrna = i.strip().split('\t')[-1]
            a[gene] = mrna
    with open(file2, 'r') as f2:
        for i in f2:
            strand = i.strip().split('\t')[-1].split(',')
            gene = i.split('\t')[-4]
            total = i.strip().split('\t')
            if len(strand) >= 2:
                total[-2] = 'mRNA,lncRNA'
                total[-3] = 'N/A'
                print '\t'.join(total)
            elif gene == 'n/a':
                print i.strip()
            else:
                print '\t'.join(i.split('\t')[:12])+'\t'+a[gene]+'\t'+''.join(strand)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

