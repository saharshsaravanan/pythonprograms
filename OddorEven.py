# write a program to print the given number is odd or evem
while True:
    try:
        num = int(input("Enter a number: "))  # Prompt user for a number and convert input to integer
        if num % 2 == 0:
            print(f"You entered {num}, which is even.")  # Corrected 'Print' to 'print' and fixed concatenation
            break
        else:
            print(f"You entered {num}, which is odd.")  # Corrected 'Print' to 'print'
            break
    except ValueError:
        print("Please enter a valid number.")  # Handle non-integer inputs

