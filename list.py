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


arr = ['偶數' , '奇數']
a = 15
print(arr[a%2])         #透過這樣就可以快速印出 不用寫 if


k=[['a','b'],'c']       #陣列中允許有陣列的陣列
print(k[0][0])
print(k[0][1])
print(k[1])