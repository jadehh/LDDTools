#!/usr/bin/env python3
# -*- coding:utf-8 -*-
##########################################
# @File     : ldd_tools.py
# @Author   : jade
# @Date     : 2022/06/27 10:39:56
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
##########################################
import os
import subprocess
from jade import GetPreviousDir,GetLastDir,CreateSavePath
import shutil
class LDDTools():
    def __init__(self,binary_file):
        self.binary_file = binary_file
    def ldd(self):
        subp  = subprocess.run("ldd {}".format(self.binary_file), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ln_file_dic = {}
        for result in subp.stdout.decode().split("\n"):
            if "=>" in result:
                ld_file = result.split("=>")[0].strip()
                ln_file = result.split("=>")[1].split("(")[0].strip()
                source_file = self.get_ln_source_file(ln_file)
                ln_file_dic[GetLastDir(ln_file)] = source_file
        return ln_file_dic

    def get_ln_source_file(self,ln_file):
        subp  = subprocess.run("ls {} -l".format(ln_file), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if "->" in subp.stdout.decode():
            ln_dir = GetPreviousDir(ln_file)
            return os.path.join(ln_dir,subp.stdout.decode().split("->")[1].strip())
        else:
            return ln_file

    def save(self,output_dir):
        CreateSavePath(output_dir)
        ln_file_dic = self.ldd()
        for key in ln_file_dic.keys():
            if "/usr/local/cuda/lib64/" in ln_file_dic[key]:
                print("cuda ln file:{},无需拷贝".format(ln_file_dic[key]))
            else:
                if os.path.exists(ln_file_dic[key]):
                    shutil.copy(ln_file_dic[key],os.path.join(output_dir,GetLastDir(ln_file_dic[key])))
                    if GetLastDir(ln_file_dic[key]) == key:
                        print("{}与{}一样,pass".format(ln_file_dic[key],key))
                        pass
                    else:
                        os.system("ln -s {} {}".format(ln_file_dic[key],os.path.join(output_dir,key)))
                else:
                    print("{}文件不存在".format(ln_file_dic[key]))
                print(ln_file_dic[key], key)


if __name__ == '__main__':
    lddTools = LDDTools("/usr/local/conta_detect-1.0/python_lib/cv2.cpython-36m-x86_64-linux-gnu.so")
    lddTools.save("opencv-gpu")