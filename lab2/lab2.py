def frequency(str1):
    dict ={}
    for i in str1:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(frequency("however"))                
    