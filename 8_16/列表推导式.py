vec1=[2,4,6]
vec2=[4,3,-9]
print([x*y for x in vec1 for y in vec2])

#嵌套复杂表达式或嵌套函数
print([str(round(355/133,i))for i in range(len(vec1))])
