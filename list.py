list = [1,7,11,5]

for i in list:          #此為印出 list 裡面的數值，非印出 list[i] 的 i
    print(i)


def Max(l):
    max = 0
    for i in range(0,len(l)):
        if(l[i]>max):
            max = l[i]
    return max
print("Max:",Max(list))  