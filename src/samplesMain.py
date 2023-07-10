#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : samplesMain.py
# @Author   : jade
# @Date     : 2022/6/28 9:08
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from src.ldd_tools import LDDTools
def main(binary_file,output_dir):
    lddTools = LDDTools(binary_file)
    lddTools.save(output_dir)