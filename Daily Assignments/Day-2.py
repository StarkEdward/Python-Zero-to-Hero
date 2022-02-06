# Lottery Prize Project
from collections import Counter         # importing Module

x = input("Enter a String: ").upper()
print("\nWelcome to the Lottery.\n\n\t", x)
x = x.lower().replace(" ", "")
ip = input("\nTo win the Lottery.\nChoose the any letter from the above word: ").lower()
s_ip = x.find(ip[0])    # index number of letter in x
'''
if you dont want to import Module you can use below method.
d = {}   # black dictionary
for i in x:
     d[i] = d.get(i, 0) + 1
'''
d = dict(Counter(x))
max_key = max(d, key = d.get)
if ip == max_key:
    print("\nCongratulations!\nYou won the Lottery Prize.")
else:
    print("\nSorry! You didn't win the Prize.")
