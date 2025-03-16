# write a program to print the given number is odd or even
# Assume user will enter only number

num = int(input("Enter a number "))
result = "The given number is "
if num %2 == 1:
    print(result +"  odd. "  )
else :
    print(result + "even.")
