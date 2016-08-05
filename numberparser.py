import re

print("This is a phone number parser.")
print("Type in the name of the file you want to parse:\n")
filename = input("> ")

phoneregex = re.compile(r'''
(\+\d)?
(-)?
(\d{3}|\(\d{3}\))?
(\.|-|\s)?
(\d{3})
(\.|-|\s)
(\d{4})
''', re.VERBOSE)

with open(filename, 'r') as filename:
    phonemo = phoneregex.findall(filename.read())

print("Phone numbers: \n")
for pn in phonemo:
    for group in pn:
        print(group, end='')
    print()