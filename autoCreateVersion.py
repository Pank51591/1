import os
import sys
 

def git_describe():
    r = os.popen("git describe --always --dirty")  
    text = r.read()  
    r.close()  
    return text.splitlines()[0]



if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("缺少设备型号 !!!")
    else :       
        ver=git_describe()
        code="#ifndef _AUTO_CREATE_VERSION_H_\n"+ \
        "#define _AUTO_CREATE_VERSION_H_\n\n"+ \
        "#define AUTO_VERSION_STR    "+"\""+sys.argv[1]+"-"+ver+"\""+"\n\n"+ \
        "#endif\n"

        f=open("./autoCreateVersion.h", mode='w')
        f.write(code)
        f.close()
