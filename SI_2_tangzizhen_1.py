num = {101,95,33,44,70,66,23,88,19,90} #定义一个集合

key1 =[] #
key2 =[]

for i in  num:
    if i >= 66:
        key1.append(i)
    if i < 66:
        key2.append(i)

key = {"key1": key1} #创建字典

key["key2"] = key2 #将小于66的添加并赋值到key2

print(key)   #打印结果