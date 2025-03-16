# Write a program to find the greatest of 3 numbers. use elif and if and else

num_1 = int(input("Enter your 1st favorite number"))
num_2 = int(input("Enter your  2nd favorite number"))
num_3 = int(input("Enter your 3rd  favorite number"))
if num_1 <= num_2 < num_3:
    print("Your third favorite number is greatest and is " + str(num_3))
elif num_2 > num_1:
    print("Your  2nd favorite number is greatest and is " + str(num_2))
elif num_1==num_2==num_3:
    print("Your 1st favorite number is equal to the rest and is " + str(num_1))
else:
    print("Your 1st favorite number is greatest and is " + str(num_1))