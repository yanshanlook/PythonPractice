dic1= dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic1)

#字典推导
dic2={x:x**2 for x in (2,4,6)}
print(dic2)

#使用关键字参数指定键值对
dic1= dict(sape=4139, guido=4127, jack=4098)
print(dic1)