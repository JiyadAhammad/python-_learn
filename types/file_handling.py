## File Handling
"""
Absolute and relative path
/user/jiyad/file_name.txt -> Absolute path
user/jiyad/file_name.txt -> relative path
"""

# here we add absolute or relative path
# Default read file
# r -> read, a-> append, w -> write, x -> Create file
import os  # operating system tasks

obj = open("test_file.txt")
result = obj.read()
print(result)

obj.close()  # clear from memmeory -> avoid memmory leak
obj = open("test_file.txt", "w")
result = obj.write("new data added")
print(result)

obj.close()  # clear from memmeory -> avoid memmory leak
obj = open("test_file.txt", "r+")  # used for read and write


os.remove("test_file.txt")  # file delted from path
