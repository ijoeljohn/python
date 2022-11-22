a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lst =[]
for i in a:
    if i in b:
        lst.append(i)

for i in lst:
    if lst.count(i)>1:
        lst.remove(i)   

print(lst)             