matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

matrix2=[[row[i]for row in matrix]for i in range(4)]
print(matrix2)

#另法
transposed=[]
for i in range(4):
    transposed.append([row[i]for row in matrix])

print(transposed)

#另法
transposed=[]
for i in range(4):
    transposed_now=[]
    for row in matrix:
        transposed_now.append(row[i])
    transposed.append(transposed_now)

print(transposed)