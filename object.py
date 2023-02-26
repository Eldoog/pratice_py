# 萬物皆物件
# 名稱 = 物件 
# 物件有型別 + 值

a = 3                # a is name, not object; 3才是
b = a                # 將右邊的物件賦予給左邊的名稱, 但是 a is not object, 而是會去 a 裡找他的物件 3 賦予給 b

print(id(a))         # print id will return  object info
print(id(b))         # 因為 b and a object is same, so id is same