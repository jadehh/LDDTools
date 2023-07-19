#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : packing.py
# @Author   : jade
# @Date     : 2022/6/28 9:44
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :

from jade import *
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--extra_sys_list', type=list,
                        default=[])  ## sys.path.append需要额外打包的路径

    parser.add_argument('--extra_path_list', type=list,
                        default=[])  ## 需要额外打包的路径
    parser.add_argument("--head_str",type=str,default="from __future__ import annotations\nimport secrets\n")
    parser.add_argument('--use_jade_log', type=str,
                        default="True")  ##是否使用JadeLog
    parser.add_argument('--full', type=str,
                        default="True")  ## 打包成一个完成的包
    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效

    parser.add_argument('--app_version', type=str,
                        default=get_app_version())  ##需要打包的文件名称
    parser.add_argument('--app_name', type=str,
                        default="LDDTools")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="LDDTools")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="False")  ## 是否打包成AppImage
    parser.add_argument('--lib_path', type=str, default="")  ## 是否lib包分开打包
    parser.add_argument('--is_qt', type=str, default="False")  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument("--zip_lib",type=str,default='False')
    parser.add_argument('--main', type=str, default="from src.samplesMain import main\n"
                                                    "import os\n"
                                                    "import argparse\n"
                                                    "if __name__ == '__main__':\n"
                                                    "\tparser = argparse.ArgumentParser()\n"
                                                    "\tparser.add_argument('-binary_file', type=str, help='please input binary_file')\n"
                                                    "\tparser.add_argument('-output_dir', type=str, help='please input output_dir')\n"
                                                    "\targs = parser.parse_args()\n"
                                                    "\tif args.binary_file is None or args.output_dir is None :\n"
                                                    "\t\tprint('请输入指定的参数')\n"
                                                    "\t\tos._exit(0)\n"
                                                    "\telse:\n"
                                                    "\t\tmain(args.binary_file,args.output_dir)\n")

    args = parser.parse_args()
    build(args)
    packAPP(args)
    zip_lib_package(args)
