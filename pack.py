import time
import pack_tri
import json

print("this path is in pack ...")

# 获取json  start  =======
def get_json_file(filename):
    f = open(filename, encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    return setting

map_key =  get_json_file("pack.json") #打包后是在上一级
print(map_key)



pack_tri.mian_method()

time.sleep(3)

print("end ...")


# import os  
# import sys  
  
# currPath = sys.path[0]  
# highPath = os.path.split(currPath)  
# print(os.path.split(currPath))  
# print(os.listdir(highPath[0])) 

# time.sleep(10)


# pyinstaller --onefile CheckLicenseEx.py 
