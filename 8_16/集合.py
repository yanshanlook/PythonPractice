#集合：无序不重复
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

print('orange'in basket)

a=set('abracadabra')
b=set('alacazam')
print(a)#a中唯一的字母
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

#集合也支持推导式
a={x for x in 'abracadabra'if x not in 'abc'}
print(a)
