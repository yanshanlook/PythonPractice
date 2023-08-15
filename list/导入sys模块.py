import sys
print("=======pythong import mode=======")
print("命令行参数为：")
for i in sys.argv:
    print(i)

print('\n python 路径为',sys.path)



#导入sys模块的argv，path成员
from sys import argv,path
print('========python from import========')
print('path:',path)
