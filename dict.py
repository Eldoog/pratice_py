# list 的使用
list = [1,2,3,4,5,6,7,8,'9']

print(list[8])                                  # index -> value
#print(list['9'])                               # value -> index ,因為是 list 沒辦法由 value 找到 index

arr = [None, None, None, None, None, None,  9]  # list 若要 print arr[6] 的值需要先定義前面 5 個的值
print(arr[0])
print(arr[6])

# list vs dict
l=['a','b']                       # list 因為寫死所以不用編號
d={0:'a', 1:'b', 9:'c'}           # dict 需要自己編號

print(l[0])                       
print(d[0])
print(l[9])
print(d[9])                       # 沒有定義，list 的缺點需要一一賦予數值

print(l[-1])                      # list 中由右往左第一個數值 -> 倒數第一個

#dict 的新增
d={1:'a', 0:'b'} 
print(d)
d[5]=9                            # dict 直接在末置位做新增
print(d)

#計算 list 裡的數值出現次數
l = [3,9,1,2,3,7,9,8,11]
d={}

for x in l:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)

for x in l:
    d[x] = d.get(x,0)+1           # 如果 get 到 x 值則 +1 ; 無的話為預設值 0
print(d)
