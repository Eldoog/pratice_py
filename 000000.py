l = [3,9,1,2,3,7,9,8,11]
d={}

for x in l:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)

for x in l:
    d[x] = d.get(x,0)+1     #如果 get 到 x 值則 +1 ; 無的話為預設值 0
print(d)
