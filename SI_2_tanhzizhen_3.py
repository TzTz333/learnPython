num=[7,5,3,1,2,0,9,4,11,13]

a=[]   #创建一个空列表用来存储结果

for i in range(len(num)): #用len函数，访问整个列表
    for j in range(i+1, len(num)):
        if i+j == 9:
            a.append((i, j)) #以元组的形式增加到列表中，增加到列表中是因元组中的数据不能修改

print(a)   #打印结果