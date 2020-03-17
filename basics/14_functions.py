# def is keyword used for defining a function


def say_hi(name, age):   # any thing after this line is going to be the body of the function
    print(f"Hi! {name}, you are {age}")  # indent is mandatory, else python will consider it as end of func


def add(num1, num2):
    return num1 + num2


say_hi("Abhishek", 30)
print(add(5, 5))
