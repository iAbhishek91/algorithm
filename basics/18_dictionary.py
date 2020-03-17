# dictionary are represented by flower braces
# they are key-value pair just in JS
# Keys are unique, same as JS
month = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
}

print(month)
print(month["Jan"])
print(month.get("Jan"))
print(month.get(4))
print(month.get("Dec"))  # returns None by default
print(month.get("Dec", "Custom default value: not a valid key"))  # returns "custom default .....
