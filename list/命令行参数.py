import sys
print("参数个数为：",len(sys.argv))
print("参数列表：",str(sys.argv))
print("脚本名：",str(sys.argv[0]))


#getopt模块
import sys
import getopt

# def site():
#     name=None
#     url=None
#     argv=sys.argv[1:]
#
#     try:
#         opts,args=getopt.getopt(argv,"n:u:")
#     except:
#         print("Error")
#
#     for opt,arg in opts:
#         if opt in ['-n']:
#             name=arg
#         elif opt in ['-u']:
#             url=arg
#
#     print(name+" "+url)
#
# site()
#命令行输入不知道怎么输入