import sys
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

try:
 c = x/y
except ZeroDivisionError:
    print("Can't divide by zero brooo")
    sys.exit(1)


print(f"{x} divided by {y} is {c}")
