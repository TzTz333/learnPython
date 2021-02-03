num1=0
result1=[]

num2=0
result2=[]

dict = { "aki":"tester","ennis":"tester","nancy":"tester" ,"c":"tester","kevin": "develop" ,"tavis": "develop"}

#遍历字典的value
for i in dict.values():
    if i =="tester":
        num1+=1
    if i =="develop":
        num2+=1
for k,v in dict.items():
    if v=="tester":
        result1.append(k)  #将"tester"对应的键增加到列表中
    if v=="develop":
        result2.append(k)  #将"develop"对应的键增加到列表中

print(num1,num2) #打印结果
print(result1)
print(result2)

