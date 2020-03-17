my_num = 10

print(str(my_num))  # to string

# print(my_num + "my lucky number")  # err: int and string cant be concatenated:w


my_str_int = "4"
my_str_float = "4.5"

print(int(my_str_int))  # to int
print(int(my_str_float))  # will throw error - err: ValueError: invalid literal for int() with base 10: '4.5'
print(float(my_str_float))  # to float
