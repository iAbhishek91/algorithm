# this can also create a new file, if the file do not exists
fd = open("basics/25_sample_file.txt", "w")
if fd.writable():
    fd.write("Jaguar - black (write)\n")  # this will be new content of the file
fd.close()


fd = open("basics/25_sample_file.txt", "a")
if fd.writable():
    fd.write("Jaguar - black (append)\n")  # this will be new content in the file
fd.close()
