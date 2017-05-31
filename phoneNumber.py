import re
import pyperclip

findPhone = re.compile(r'''
(\d{3}|\(\d{3}\)) #area code
(\s|-|\.) #separator
(\d{3}) #3 digits
(\s|-|\.) #separator
(\d{4}) #4 digits
''', re.VERBOSE)

findEmail = re.compile(r'([a-zA-Z0-9._-]+)(@.*\.com)')

text = str(pyperclip.paste())

contactList = []

for groups in findPhone.findall(text):
    phone = groups[0]+'-'+groups[2]+'-'+groups[4]
    contactList.append(phone)
for groups in findEmail.findall(text):
    email = groups[0]+groups[1]
    contactList.append(email)

print contactList

if len(contactList) > 0:
    pyperclip.copy('\n'.join(contactList))
    print('Contatcs copied to clipboard.')
    print('\n'.join(contactList))
else:
    print('No contact found.')

