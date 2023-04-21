# 
#  Copyright (c) 2021, Xiaojin.Zheng
# 
#  SPDX-License-Identifier: Apache-2.0
# 
#  Change Logs:
#  Date             Author                  Notes
#  2021-06-01       Xiaojin.Zheng           first add
# 

import os
import sys
import shutil

def execCmd(cmd):  
    r = os.popen(cmd)       #从一个命令打开一个通道， 返回一个文件描述符号为fd的打开的文件对象
    text = r.read()       
    r.close()  
    return text

def rename(path):
    dir,file=os.path.split(path)         #分割目录名（dir）和文件名(file)   （得到一个列表，包括目录和文件后缀）
    file_name=os.path.splitext(file)[0]  #文件名
    file_suffix=os.path.splitext(file)[-1]    #后缀名
    ver=execCmd("git describe --tags --always --dirty").splitlines()[0]        #获取版本说明  （只取列表里面的第一个元素，即版本号）
    if( file_name == "Jupiter_120VAC_60Hz"):
        new_path=os.path.join(dir,"HT-SOFTWARE-824-A2105A-V01"+"-内部版本-"+ver+"("+file_name+")"+file_suffix)    #将目录名与文件名合并
    elif( file_name == "Jupiter_230VAC_50Hz"):
        new_path=os.path.join(dir,"HT-SOFTWARE-824-A2105B-V01"+"-内部版本-"+ver+"("+file_name+")"+file_suffix)
    else :
        print("rename fail")
        return
    shutil.copy(path,new_path)      #将源文件中的内容复制到目标文件或目录
    print(new_path)


if __name__ == "__main__":
    if(len(sys.argv) < 2):       #命令行参数的个数
        print("file name unfound")
    else :
        rename(sys.argv[1])         #sys.argv[1]   从命令行参数里面获取路径
