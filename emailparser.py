import re

print("This is an email parser.")
print("Type in the name of the file you want to parse:\n")
filename = input("> ")

emailregex = re.compile(r'''
([a-z0-9\.]+)
(@)
([a-z0-9\.]+)
(\.)
([a-z]{2,4})
''', re.VERBOSE | re.IGNORECASE)

with open(filename, 'r') as filename:
    emailmo = emailregex.findall(filename.read())

print("Emails: \n")
for email in emailmo:
    for group in email:
        print(group, end='')
    print()