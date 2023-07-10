#!/usr/bin/env python3
# -*- coding:utf-8 -*-
##########################################
# @File     : main.py
# @Author   : jade
# @Date     : 2022/06/27 10:39:34
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
##########################################
from src.samplesMain import main
import os
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-binary_file', type=str, help='please input binary_file')
    parser.add_argument('-output_dir', type=str, help='please input output_dir')
    args = parser.parse_args()
    if args.binary_file is None or args.output_dir is None :
        print('请输入指定的参数')
        os._exit(0)
    else:
        main(args.binary_file,args.output_dir)