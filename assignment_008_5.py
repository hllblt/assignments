# sum1 = 1
# sum2 = 1
fibonacci = [sum1,sum2]
while sum2 < 55:
    sum1,sum2 = sum2,(sum1+sum2)
    fibonacci.append(sum2)
print(fibonacci)
