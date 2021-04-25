number = input("Enter a positive whole number: ")
armlist = []
sum = 0
if number.isdigit() == True:
    for i in number:
        armlist.append(int(i))
    for i in armlist:
        sum += i**len(number)
    if sum == int(number):
        print(f"{number} is an Armstrong Number!")
    else:
        print(f"{number} is not an Armstrong Number!")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
