# dictionarys

# -------------------------------
# Example 1
# -------------------------------

# dictionarys are used to store colloections of object like string or tuples
# however it stores the infomation in pairs called key-value pairs
phonebook = {"Jenny" : "867-5309", "Mike Jones": "281-330-8004",
             "Destiny": "900-783-3369"}
print(phonebook)

# NOTE Python sorts the contents of the dictionary in a way that makes it
# very fast to get information out of the dictionary (by a process
# called hashing), but this ordering changes randomly every time the
# contents of the dictionary change.

# the important feasture of dictionarys is the paired value of each item in
# in the list by specifying a key
print(phonebook["Jenny"])

# new keys can be added to a dictionary by spefying and new key and assigning a
# value
phonebook["Obama"] = "202-456-1414"
print(phonebook)

# deleting values can use the del() function
del(phonebook["Jenny"])
print(phonebook)

# keys() can be used to extract all the key values in a dictionary this is
# is useful when we need to loop over the keys
print(phonebook.keys())

# NOTE the returned value is a dict_keys object not a list so has diffrent
# methods available to it it is converted to a list using list()
