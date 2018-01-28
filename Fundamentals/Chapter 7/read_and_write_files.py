# -------------------------------
# Example 1
# -------------------------------

# if we want ot work with a lot of data it's usefeul to keep it in a seperate
# raw text file it can be created and written to using the open("name.txt", "w")
output_file = open("hello.txt", "w")
output_file.writelines("Test file hahaha\n") # writes string to text file
output_file.writelines("Does this end up on the nest line?")
output_file.close() # remember to close files when finished with them

output_file = open("file2.txt", "w")
linesToWrite = ["Test file hahaha", "2" , "test"] # useful to store data you want to write
output_file.writelines(linesToWrite) # then write it
output_file.close()

output_file = open("file2.txt", "a")
linesToWrite = ["\nTested file\n", "25\n" , "tested\n"] # useful to store data you want to write
output_file.writelines(linesToWrite) # then write it
output_file.close()

# NOTE opening a file using "w" deletes it's entire contents and the writes
# the new data use the "a" to add data to an already exising file


# -------------------------------
# Example 2
# -------------------------------

# files can be read using using .readlines() and open thee file using "r"
output_file = open("file2.txt", "r")
print(output_file.readlines())
output_file.close()
