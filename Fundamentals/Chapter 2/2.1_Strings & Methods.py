# First script yay

'''
Multi
Line
Comments
'''

phrase = 'Hello Wolrd'

# both types of quotation marks can be used to define strings
# allowing "" or ' to be used within strings

quote_test_1 = "This is the President's Milk"
quote_test_2 = 'As the great man once said "This is milk for the President"'

print(quote_test_1, quote_test_2)

# Inital creation of longer phrase veriable
longerphrase = '''This is a multiline
string that spans across multiple lines '''

# Redefines longerphrase veriable to new string
# Muli line comments cannot appear on the same line as multi line strings
longerphrase = ''' This is the new multi line
litteral that spans across multiple lines '''

print(phrase)
print(longerphrase)

# the make multi line strings print on a single line use \ when writing it out
even_longer_phrase = "this is a multi line comment test \
oh wow how good is this"

print(even_longer_phrase)
