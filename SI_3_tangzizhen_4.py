from datetime import datetime
dt = datetime.now()   #创建一个datetime类对象

#打印时间
print(f"今天是：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}")

#在文件中写入时间
f = open('time.txt','a')
f.write("\n")
f.write(f"今天是：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}")
f.close() #关闭文件
