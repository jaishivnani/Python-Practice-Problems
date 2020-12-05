
a = 5
b = 2

try:
    k = int(input("Enter a number"))
    print(k)
    print("resource open")
    print(a/b)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong...")

finally:
    print("resource closed")



