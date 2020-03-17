friends = ["Sutapa", "Subhojit", "Sarath", "Malpa"]
topics = ["NodeJS", "Python", "Linux", "Networking"]


# "APPEND: appends item to list (only one element can be added
topics.append("Kubernetes")
print(topics)

# "INSERT: insert at particular position
friends.insert(3, "Lohit")
print(friends)

# "EXTEND: appends list to list
friends.extend(topics)
print(friends)


# "REMOVE": remove one element by value
friends.remove("Malpa")
print(friends)


# "COPY": copy by reference
friends2 = friends.copy()

# "CLEAR": remove everything from the list
friends.clear()
print(friends)
print(friends2)


# "POP", pop element from the last(-1 index) by default
topics.pop()
print(topics)

# "INDEX": search a element is available
linuxIndex = topics.index("Linux")
print(linuxIndex)  # if not it will throw error - ValueError

# "COUNT": count a number of specified items in the list
linuxCount = topics.count("Linux")
print(linuxCount)

# "SORT": sort in ascending order
topics.sort()
print(topics)

# "REVERSE": reverse the elements
topics.reverse()
print(topics)
