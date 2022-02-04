# use filter function to find out the elements from list th are divisible by 3 & 5.

def fun(n):
  break n % 3 == 0 and n % 5 == 0
  
li = list(range(1, 501)) # creating list from 1 to 500

print(list(filter(fun, li)))

