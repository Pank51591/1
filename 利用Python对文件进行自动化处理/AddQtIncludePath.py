#
# Copyright (c) 2021, Xiaojin.Zheng
#
#  SPDX-License-Identifier: Apache-2.0
# 
#  Change Logs:
#  Date             Author                  Notes
#  2021-07-01       Xiaojin.Zheng           First add
#

import os

def list_pro_files(folder_path):
    pro_files=[]
    file_list=os.listdir(folder_path) #返回path指定的文件夹包含的文件或文件夹的名字的列表
    #print(file_list)
    for file in file_list:
        if file.split(".")[-1] == "pro":# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
            pro_files.append(file) #向列表末尾追加元素
    return pro_files


#生成包含路径
def generate_include_path(pro_file):
    header_lines=[]
    include_path_lines=[]
    last_line=""
    is_header_part=False
    #get all header lines
    fd=open(pro_file,"r")
    for line in fd.readlines():    #for in 经常用于遍历字符串、列表，元组，字典等
        if "HEADERS" in line:
            is_header_part=True
        elif "SOURCES" in line:
            break
        elif is_header_part==True and line != last_line:
            header_lines.append(line)
            last_line=line
    fd.close()
    #header line to include line
    last_line=""
    for line in header_lines:
        #get file name and to end
        path=line.split(line.split("/")[-1])[0] + " \\\n"
        if last_line != path:
            #print(path)
            include_path_lines.append(path)
            last_line=path
    del include_path_lines[-1]
    include_path_lines.append("\n")
    include_path_lines.append("\n")
    #print(include_path_lines)
    return include_path_lines


def add_new_include_path(pro_file,include_path):
    file_lines=[]
    is_includePath_part=False
    fd=open(pro_file,"r")
    for line in fd.readlines():
        if "INCLUDEPATH" in line:
            is_includePath_part=True
        elif "HEADERS" in line:
            is_includePath_part=False
            file_lines.append("INCLUDEPATH += \\\n")
            for path_line in include_path:
                file_lines.append(path_line)
            file_lines.append(line)
        elif is_includePath_part==False:
            file_lines.append(line)
    fd.close()
    #print(file_lines)
    fd=open(pro_file,"w")
    for line in file_lines:
        fd.write(line)
    fd.close()
    return file_lines



def add_include_path(folder_path):
    pro_files= list_pro_files(folder_path)
    for file in pro_files:
        include_path=generate_include_path(file)
        add_new_include_path(file,include_path)
        


if __name__ == '__main__':
    add_include_path(".")   #使用当前文件夹路径
