array = [1, 40, 20, 3, 5, 61, 62, 7, 8]


def first_repetitive_element(arr):
    length = len(arr)
    ptr_index_one = 0
    ptr_index_two = 1
    while ptr_index_two < length:
        if arr[ptr_index_one] == arr[ptr_index_two]:
            return arr[ptr_index_one]

        ptr_index_one += 1
        ptr_index_two += 1

    return -1


print(first_repetitive_element(array))
