

is_male = True

if is_male:
    print("MALE")

is_male= False

if is_male:
    print("MALE")
else:
    print("Not MALE")


is_tall = True

if is_male and is_tall:
    print("tall and male")
elif is_male and not(is_tall):
    print("short and male")
elif not is_male and is_tall:
    print("tall and not male")
else:
    print("Neither tall nor male")
