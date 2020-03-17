
fd = open("basics/24_sample_file.txt", "r")  # r, r+(read write), w, a
if fd.readable():
    # once we use a file descriptor, the read file is moved, and will not read the previous lines
    # hence do not use all the below function together.
    print(fd.read())  # read entire line
    print(fd.readline())  # read single line
    print(fd.readline())  # read second line
    print(fd.readlines())  # read individual lines and put it in a array
    print(fd.readlines()[1])  # read second element from the array, basically second line
    # for loop to go through the file lines
    for line in fd.readlines():
        print(line)
fd.close()
