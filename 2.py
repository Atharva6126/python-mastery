# Welcome to the day 2 of my project in python. Today we'll build a grading system 

print("This is a Grading System...")
m = int(input("Enter your marks: "))

if m >= 90 and m <= 100:
    print("S")
elif m >= 80 and m <= 89:
    print("A")
elif m >= 70 and m <= 79:
    print("B")
elif m >= 60 and m <= 69:
    print("C")
elif m>= 50 and m <= 59:
    print("D")
else:
    print("E")
