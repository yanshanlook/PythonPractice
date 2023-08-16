#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

#同时遍历两个或更多的序列，可以使用 zip() 组合
questions= ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print("What is your {}? It is {}".format(q,a))

#反向遍历
for i in reversed(range(1,10,2)):
    print(i)

#按顺序遍历
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)