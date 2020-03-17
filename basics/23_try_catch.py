try:
    num = int(input("enter a number: "))
    print(num)
except ValueError as e:
    print(f"invalid input: {e}")
except ZeroDivisionError as e:
    print(f"division by 0 is not allowed: {e}")
