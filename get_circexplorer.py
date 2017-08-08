#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-08-06 20:53:05
import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            chrom = i.split('\t')[0]
            start = i.split('\t')[1]
            end = i.split('\t')[2]
            strand = i.split('\t')[5]
            junc = i.split('\t')[9]
            cir = chrom + ':' + start + '|' + end
            print cir + '\t' + junc + '\t' + '_'.join(sys.argv[1].split('_')[:2]) + '\t' + 'circexplorer' + '\t' + strand


if __name__ == '__main__':
	main(sys.argv[1])


