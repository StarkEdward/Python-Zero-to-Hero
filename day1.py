# Take multiple number as input and print sum.
num = [int(i) for i in input("Enter the values: ").split()]
total = 0
for add in num:
    total += add
print(f"The sum of all Number is: {total}")