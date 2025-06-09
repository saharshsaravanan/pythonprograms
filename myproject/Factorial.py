# write a program to find factorial of a given number by user.
import sys
from math import factorial

sys.set_int_max_str_digits(999999)
num=int(input("Enter a number"))
total=1
while num>0:
    total=factorial(num*total)
    num-=1
print(total)

