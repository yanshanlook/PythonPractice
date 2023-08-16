for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=" ")
    print(repr(x**3).rjust(4))
#字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格

import math
print("常量π的值近似为：{:.3f}".format(math.pi))


# file=open("test.txt",'w')
# file.write("python是一门非常好的语言。\n是的，的确非常好！！\n")
#
# file=open("test.txt","r")
# str=file.read()
# print(str)
# file.close()

# file=open("test.txt",'r')
# str=file.readlines()#读取所有行
# print(str)

f=open("test.txt",'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
print(f.read(2))


