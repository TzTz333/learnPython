def main(n):
    sum = 0
    for i in range(1,n+1): #进行循环以计算数值
        a = 2*i-1
        sum += a
    return sum
x = int(input('n='))  # 可以自由输入n的数值
result = main(x)
print(result)  #输出结果

