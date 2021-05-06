number = int(input("Enter a positive whole number: "))
primelist = []
for p in range(2,number):
    i = 2
    while i <= p:
        if (p%i != 0) and (p != i):
            i += 1
        elif p == i:
            primelist.append(p)
            i += 1
        else:
            break
print(primelist)
