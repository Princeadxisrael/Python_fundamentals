import os

# open(filename, mode)
#"r"- reading files
# "a" -appends to an existing file or create a new file if does not exist
# "w"- opens up a file for writing
# "x"- creates a specified file, return an err if file already exist

# "t"- Text- 
# "b"- Media files

# f=open("init/Python.txt", "r")
# # print(f.readline())
# # print(f.readline())

# for x in f:
#     print(x)

# f.close()

f=open("init/Python.txt", "a")

f.write("Writing more content to this file")

f.close()

f=open("init/Python.txt", "r")
print(f.read())
f.close()

f=open("init/Python2.txt", "a")
f.write("This file now has content")
f.close()

f=open("init/Python2.txt", "r")
print(f.read())
f.close()

f=open("init/Python.txt", "w")
f.write("I have deleted everything here")
f.close()

f=open("init/Python.txt", "r")
print(f.read())

# f=open("myfile.txt", "x")

os.remove("myfile.txt")
f.close()




