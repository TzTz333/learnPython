n=17
for j in range(-int(n / 2), int(n / 2) + 1):
    print(" " * abs(j), "* " * abs(int(n/2)+1 - abs(j)))
print('\n')


line = 9
for x in range(0, line) :
    print(" " * (line - x),end = " ")
    print("* " * (x + 1))
