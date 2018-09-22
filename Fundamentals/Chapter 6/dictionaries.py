# dictionaries

# -------------------------------
# Example 1
# -------------------------------

# dictionaries are used to store colloections of object like string or tuples
# however it stores the infomation in pairs called key-value pairs
phonebook = {"Jenny": "867-5309", "Mike Jones": "281-330-8004",
             "Destiny": "900-783-3369"}
print(phonebook)

# NOTE Python sorts the contents of the dictionary in a way that makes it
# very fast to get information out of the dictionary (by a process
# called hashing), but this ordering changes randomly every time the
# contents of the dictionary change.

# the important feature of dictionaries is the paired value of each item in
# in the list by specifying a key
print(phonebook["Jenny"])

# new keys can be added to a dictionary by specifying and new key and assigning a
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


# -------------------------------
# Example 2
# -------------------------------

# To preform an operation on all the keys in a dictionary we can use a for
# loop the dictionary will be accessed in it's hashed order
for contact_name in phonebook:
    print(contact_name, phonebook[contact_name])

# we can use in to check if a key exists in a dictionary
print("Jenny" in phonebook)
print("Obama" in phonebook)

# NOTE it's important to use in statement as requesting a dictionary key
# that does not exist will throw an error.

# to acess the dictioary in its sorted order the sorted function is used
for contact_name in sorted(phonebook):
    print(contact_name, phonebook[contact_name])

# dictionary values can be any object type (including other dictionaries)
# but keys must be immutable objects
contacts = {"Jenny": {"cell": "555-0199", "home": "867-5309"},
            "Mike Jones": {"home": "281-330-8004"},
            "Destiny": {"work": "900-783-3369"}}
print(contacts)
print(contacts["Jenny"]["cell"])

# alternative ways to create dictionaries
# dict() can be used to create dictionaries where key names will only contain
# strings and numbers
test_dictionary = dict(string1="value1", string2=2, string3=3.0)
print(test_dictionary)

# we can also provide the pairings provided as tupples
simple_dictionary = dict(
    [("string1", "value1"), ("string2", 2), ("string3", 3.0)])
print(simple_dictionary)


# *******************************
# Exercises
# *******************************

# Ex 1
birthdays = {}

# Ex 2
birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

# Ex 3
names_list = ['Yoda', 'Darth Vadar']

for name in names_list:
    if name in birthdays:
        pass
    else:
        birthdays[name] = 'unknown'

print(birthdays)

# Ex 4
for keys in birthdays:
    print(f"{keys} {birthdays[keys]}")

# Ex 5
del(birthdays['Darth Vader'])

# Ex 6
birthdays = dict([('Luke Skywalker', '5/24/19'), ('Obi-Wan Kenobi', '3/11/57'),
                  ('Darth Vader', '4/1/41')])
