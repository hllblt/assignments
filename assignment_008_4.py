number = int(input("Enter a positive whole number: "))
i = 2
while True:
    if (number%i != 0) and (number != i):
        i += 1
    elif number == i:
        print(f"{number} is a prime number")
        break
    else:
        print(f"{number} is not a prime number")
        break
