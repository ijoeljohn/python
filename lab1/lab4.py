num = int(input("Enter a number"))
divisor = []

for i in range(1, num):
    if num % i ==0:
        divisor.append(i)
print(divisor)