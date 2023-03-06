list = [1,7,11,5]

for i in list:          #此為印出 list 裡面的數值，非印出 list[i] 的 i
    print(i)

# list 新增、插入
print(list)
list.append('15')
print(list)
list.insert(1,'2222')
print(list)


arr = ['偶數' , '奇數']
a = 15
print(arr[a%2])         #透過這樣就可以快速印出 不用寫 if


k=[['a','b'],'c']       #陣列中允許有陣列的陣列
print(k[0][0])
print(k[0][1])
print(k[1])