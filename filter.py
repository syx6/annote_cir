#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            sample = i.split('\t')[2]
            if 'T' in sample:
                if 'N' in sample:
                    print 'cancer,normal' + '\t' + i.strip()
                else:
                    print 'cancer' + '\t' + i.strip()
            else:
                print 'normal' + '\t' + i.strip()


if __name__ == '__main__':
    main(sys.argv[1])