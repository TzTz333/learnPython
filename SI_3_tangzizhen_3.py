f = open('3_3.txt','a')  # 如果filename不存在会自动创建， ’w’, ‘a’, 分别表示擦除原有数据再写入和将数据写到原数据之后
f.write("\n")
f.write("url:https://www.google.com/,e-mail:maker@163.com,usernamfore:maker\n")
f.close() #关闭文件

#打开文件，读取文件中每行数据的信息
f = open('3_3.txt', 'r')
f.seek(0,0)  #移动文件指针
list=[]
j=1
m=len(f.readlines()) #文件里的行数
print(m)

f.seek(0)

while j<=3:    #将信息以字典方式输出
    dict={}
    content=f.readline()
    a=content.split(',')
    for i in range(len(a)):
        b=a[i].split(':',1)
        c=b[1].splitlines()
        dict[b[0]]=c[0]

    list.append(dict)
    j+=1
print(list)
f.close()