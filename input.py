#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            cir = i.split('\t')[1]
            chrom  = cir.split(':')[0]
            start = cir.split(':')[1].split('|')[0]
            end = cir.split(':')[1].split('|')[1]
            sample_type = i.split('\t')[0]
            junc = i.split('\t')[2]
            sample = i.split('\t')[3]
            tools = i.split('\t')[4]
            strand = i.split('\t')[5]
            sprtm = i.strip().split('\t')[-1]
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (sample, cir, chrom, start, end, junc, strand, tools, sprtm, sample_type))


if __name__ == '__main__':
    main(sys.argv[1])