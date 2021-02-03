str1 =  "ayjayjabcdefghfqeweewofgfsadglkfhhds"
list = []

#字符串——>列表
for str in str1:  #遍历字符串
    list.append(str)   #将字符串的值增加到列表中

    dict = {}        #创建一个字典

for i in list:  #循环，查找重复的字母
    if list.count(i) >= 1:
        dict[i] = list.count(i)

print(dict)



