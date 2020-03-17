arr = [2, 3, 9, 13, 99, 1, 50, 25, -8]


def lowest_in_array(list):
    list.sort()
    return list[0]


print(lowest_in_array(arr))
