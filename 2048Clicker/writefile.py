with open("C:/Users/Sahar/FIRST.txt.txt","r") as file:
    content = file.read()
    print(content)
    uppercontent = ""
    for letter in content:
        if letter.isalpha():
            letter = letter.upper()
        uppercontent += letter
print(uppercontent)
with open("C:/Users/Sahar/FIRST.txt.txt","w") as file:
    file.write(uppercontent)



