def factorial(n):
    fact = 1
    while 1 < n:
        fact = fact * n
        n -= 1
    print("Factorial is :", fact)
    
factorial(int(input("Enter a number: ")))