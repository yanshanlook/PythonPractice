list=['abcd',786,'runoob',70.2]
tinylist=[123,'runoob']
print(tinylist*2)
#*是重复操作
print(list+tinylist)

tuple=(list,tinylist)
tuple[0][0]='abc'
print(tuple)