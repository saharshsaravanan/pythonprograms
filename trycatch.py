# write a sample program to illustrate try, except and finally
try:
    num=int(input("Enter a number to print table"))
    i=1
    num2=int(input("Enter a number to print the table till."))
    while i<num2+1:
        print(f"{num} x {i} = {num*i}")
        i+=1
except:
    print("you entered a word not a number")
finally:
    print("I always execute")






