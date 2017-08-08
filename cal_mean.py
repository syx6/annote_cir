#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-06-22 16:22:20
import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            junc = i.split('\t')[1].split(',')
            junc1 = [int(m) for m in junc]
            mean_junc1 = sum(junc1) / len(junc1)
            sprtm = i.strip().split('\t')[-1].split(',')
            sprtm1 = [float(n) for n in sprtm]
            mean_sprtm1 = sum(sprtm1) / float(len(sprtm1))
            cir = i.split('\t')[0]
            sample = i.split('\t')[2]
            tools = i.split('\t')[3]
            strand = i.split('\t')[4]
            print cir + '\t' + str(mean_junc1) + '\t' + sample +'\t'+ tools + '\t' + strand + '\t' + str(mean_sprtm1)

if __name__ == '__main__':
    main(sys.argv[1])

