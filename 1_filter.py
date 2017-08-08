#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(file1):
    with open(file1, 'r') as f1:
        for i in f1:
            sample = i.split('\t')[2]
            if 'aizuzhi' in sample:
                if 'xueye' in sample:
                    if 'aipang' in sample:
                        print('aizuzhi,xueye,aipang' + '\t' + i.strip())
                    else:
                        print('aizuzhi,xueye' + '\t' + i.strip())
                else:
                    if 'aipang' in sample:
                        print('aizuzhi,aipang' + '\t' + i.strip())
                    else:
                        print('aizuzhi' + '\t' + i.strip())
            else:
                if 'xueye' in sample:
                    if 'aipang' in sample:
                        print('xueye,aipang' + '\t' + i.strip())
                    else:
                        print('xueye' + '\t' + i.strip())
                else:
                    print('aipang' + '\t' + i.strip())



if __name__ == '__main__':
    main(sys.argv[1])
