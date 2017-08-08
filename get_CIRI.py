#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-08-06 20:53:05
import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            if i.startswith('circRNA_ID'):
                pass
            else:
                cir = i.split('\t')[0]
                start = int(cir.split(':')[1].split('|')[0]) - 1 # gtftobed -1
                end = int(cir.split(':')[1].split('|')[1])
                chrom = cir.split(':')[0]
                total_cir = chrom + ':' + str(start) + '|' + str(end)
                junc = i.split('\t')[4]
                strand = i.split('\t')[10]
                print total_cir + '\t' + junc + '\t' + sys.argv[1].split('.')[0] + '\t' + 'CIRI' + '\t' + strand


if __name__ == '__main__':
	main(sys.argv[1])


