# -------------------------------
# Example 1
# -------------------------------

# if we want ot work with a lot of data it's usefeul to keep it in a seperate
# raw text file it can be created and written to using the open("name.txt", "w")
output_file = open("hello.txt", "w")
output_file.writelines("Test file hahaha\n")  # writes string to text file
output_file.writelines("Does this end up on the nest line?")
output_file.close()  # remember to close files when finished with them

output_file = open("file2.txt", "w")
# store data you want to write
linesToWrite = ["Test file hahaha", "2", "test"]
output_file.writelines(linesToWrite)  # then write it
output_file.close()

output_file = open("file2.txt", "a")
# useful to store data you want to write
linesToWrite = ["\nTested file\n", "25\n", "tested\n"]
output_file.writelines(linesToWrite)  # then write it
output_file.close()

# files can be read using using .readlines() and open thee file using "r" each
# line is imported as string and layed out as a list with /n for line breaks
output_file = open("file2.txt", "r")
print(output_file.readlines())
output_file.close()

# NOTE opening a file using "w" deletes it's entire contents and the writes
# the new data use the "a" to add data to an already exising file


# -------------------------------
# Example 2
# -------------------------------

# a common way to read a file is to use a for loop to process each line
input_file = open("input.txt", "r")

for line in input_file:
    print(line), # adding a comma will prevent auto /n comments

input_file.close()

# NOTE: you can change the automatic \n for somthing else using
# print(line, end="") double quotes will be blank we could add /n/n
# to create an extra line after each line

# we can also use .readlines() readlines will keep track of the last line it
# read while a file is open in "r" (read mode) and read the line after the
# last read
input_file = open("input.txt", "r")
line = input_file.readline()

while line != "":
    print(line)
    line = input_file.readline()

input_file.close()

# -------------------------------
# Example 3
# -------------------------------

# with can be used to condence the code this creates a new veriable but also a
# new code block so the closing of the text file handled automaticly
with open("hello.txt", "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line),

# we can open multiple files at one time with the withstatement
with open("hello.txt", "r") as my_input_file, open("output.txt", "w") as my_output:
    for line in my_input_file.readlines():
        my_output.write(line)

# if we want to use a specific part of a of a file the seek() function can be
# used to jump a certain number of charaters into a file.
with open("test_format.txt", "rb") as input_file:
    print ("Line 0 (first line):", input_file.readline())
    print ("Line 0 again does not work (first line):", input_file.readline())

    input_file.seek(0) # jump to beginning of the document
    print ("Line 0 can be reprinted after seek(0) (first line):", input_file.readline())

    input_file.seek(15) # jump to charater at index 15
    print ("Line 0 (starting at the 16th charater):", input_file.readline())

    input_file.seek(3, 2) # jump forward 4 charaters
    print ("Line 0 (starting at the 16th charater):", input_file.readline())

# NOTE: we can open a file for reading and writing using the r+ command seek
# aside from finding the beginning or end of file is rarely useful and hard to
# keep track of. A new seek should be preformed when switching from reading to
# writing

# *******************************
# Exercises
# *******************************
print()

# Exercise 1
print("Exercise 1")
with open("poem.txt", "r") as poem:
    for line in poem.readlines():
        print(line)

# Exercise 2
# see above

# Exercise 3
with open("output.txt", "w") as output_file, open("poem.txt", "r") as input_file:
    for line in input_file:
        output_file.writelines(line)

# Exercise 4
with open("output.txt", "w") as append_file:
    append_file.writelines("Hahahahahaha a new line")
