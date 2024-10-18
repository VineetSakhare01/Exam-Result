
# Program to input student name & marks of 3 subjects and print name & percentage

a = str(input("Enter Student Name:"))
b = int(input("How much marks did you get in English subject:"))
c = int(input("How much marks did you get in Maths subject:"))
d = int(input("How much marks did you get in Science subject:"))

a1 = b+c+d

F = a1/300*100

print(f"Congratulations {a}, you have score {int(F)}%. Well done keep growing!")