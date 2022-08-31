#basic calculator

import time

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str( b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b ) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    time.sleep(0.7)
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("input your choice: ").upper()

    if choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        time.sleep(0.7)
        add(a, b)
    elif choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        time.sleep(0.7)
        sub(a, b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        time.sleep(0.7)
        mul(a, b)
    elif choice == "D":
        print("Division" )
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        time.sleep(0.7)
        div(a, b)
    elif choice == "E":
        time.sleep(0.6)
        print("Shutting down...")
        time.sleep(1.2)
        print("Bye bye!")
        quit()
    else:
        time.sleep(0.5)
        print("""
Sorry that option is not available, try again.        
""")