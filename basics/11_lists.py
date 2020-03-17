# list are array
# this are represented using sq brackets
# declaration are done similar to normal variables
# can put any type of data (mixed)


me = ["Abhishek", 30, False, "nodejs, linux, python, networking"]

# entire list
print(me)

# specific element on the list
print(f"Hello, {me[0]}, you are {me[1]} year old, and you are {'employed' if me[2] else 'unemployed' }")

# reverse order (negative indexing)
print(f"You are {'employed' if me[-1] else 'unemployed'}")

# out of boundary
# print(me[4]) # list index out of range
# print(me[-5]) # list index out of range


#  range of element
print(me[1:])  # from 1 index to all
print(me[1:3])  # from 1 index to 2 index (excluding 2)
