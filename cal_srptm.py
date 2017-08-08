#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2017-06-05 10:52:26

import sys
import math
from collections import defaultdict


def cal_srptm(jreads, mapped_reads, length):
    srptm = math.log((jreads/(mapped_reads * length)) * (10**12), 2)
    return srptm

def main(file1, file2):
    info  = defaultdict(list)
    with open(file1, 'r') as f1:
        for i in f1:
            if i.startswith('sample'):
                pass
            else:
                sample = i.split('\t')[0]
                mapped_reads = i.split('\t')[1]
                length = i.strip().split('\t')[2]
                info[sample].append(mapped_reads)
                info[sample].append(length)
    with open(file2, 'r') as f2:
        for i in f2:
            sam = i.split('\t')[2].split(',')
            reads = i.split('\t')[1].split(',')
            exp = []
            for m, n in enumerate(sam):
                mapped_reads = float(info[n][0])
                length = float(info[n][1])
                jreads = float(reads[m])
                s_rptm = str(cal_srptm(jreads, mapped_reads, length))
                exp.append(s_rptm)
            print i.strip() + '\t' + ','.join(exp)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])



