# backslash (escape) character

print("abhishek\"s python")


# few string functions
line = "Abhishek Das is leaning Python"
print(len(line))  # 30
print(line.upper())  # ABHISHEK DAS IS LEARNING PYTHON
print(line.lower())  # abhishek das is learning python
print(line.islower())  # false
print(line[0])  # A
print(line.index("Das"))  # 9
print(line.index("a"))  # 9
print(line.replace("abhishek", "sutapa"))  # Note: case sensative O/P: Abhishek Das is leaning Python

# chaining function
print(line.upper().isupper())  # true
