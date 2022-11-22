L = ['mashuplab\n','stack\n',]

file1 = open ('L','w')
file1.writelines(L)
file1.close()

file1 = open('L','r')
lines = file1.readlines()

count = 0

for line in lines:
    count += 1
    print("line{}: {}".format(count,line.strip()))