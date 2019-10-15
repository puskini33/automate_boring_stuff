import re

"""pyperclip # install pyperclip from cmd when internet on is: pip install pyperclip"""

phone_number_regex = re.compile(r'''((\+.?\d{2})? # +00 for international numbers
                             (01)? # for national numbers
                             \(?\d{3}\)? # area code
                             (\s|-|[.])? # separator
                             \d{3} # first three digits
                             (\s|-|[.])? # separator
                             \d{4}) # last 4 digits
                             ''', re.VERBOSE)

email_regex = re.compile(r'''(
                             [a-zA-Z0-9.+-]+ # name of the person in the email
                             @ # the usual @
                             [a-zA-Z0-9.]+ # the name of the domain
                             [.]
                             [a-zA-Z]{2,4} # the extension
                             )''', re.VERBOSE)

url_regex = re.compile(r'''(
                            ^(http(s)?://)? # hyper text transfer protocol usual format
                            (w{3}\.)? # the possible world wide web syntax
                            [a-zA-Z0-9.+]+ # any type of character is matched at least once
                            (\.[a-zA-Z]{2,4})$ # the web address ends in .com or sth. similar
                            )''', re.VERBOSE)

number_regex = re.compile(r'(?<!\d,)(?<!\d)\d{1,3}(?:,\d{3})*(?!,?\d)')

date_regex = re.compile(r'''(
                        (\d{,4}) # month, day, or year
                        (\s|-|\.|/)? # separator
                        (\d{,2}) # month or day
                        (\s|-|\.|/)? # separator
                        (\d{,4}))| # year, month, or day
                        ((\d\d{,2}[a-z]{2}) # day in a text format
                        \s[a-zA-Z]{,10}\s # month in a text format
                        (20[0-50]{2}|19[0-99]{2})$) # year
                        ''', re.VERBOSE)

IBAN_regex = re.compile(r'''(
                        ([a-zA-Z]{,3}\d{2}\s)?
                        ((\d\d\d\d\s){4}|(\d\d\d\d\s){3}\d\d\d\d)
                        (\d\d)?
                                )''', re.VERBOSE)
IBAN_regex.sub(r'\2**** **** **** **** **', 'DE97 1111 2222 3333 4444 55')
IBAN_regex.sub(r'**** **** **** ****', '1111 2222 3333 4444')

social_security_number_regex = re.compile(r'''(
                                          ([a-zA-Z])?\d{8,11}
                                          )''', re.VERBOSE)
social_security_number_regex.sub(r'*********', 'D123456789')
social_security_number_regex.sub(r'*********', '123456789')


simple_password_validator = re.compile(r'^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*')

extra_space_regex = re.compile(r'(?!\n)(\s\s)')

repetition_word_regex = re.compile(r'\b(\w+)\s+\1\b')

extra_exclamation_points = re.compile(r'!+')

text = str(pyperclip.paste())
matches = []
for groups in phone_number_regex.findall(text):
    phoneNum = ' '.join([groups[1], groups[2], groups[3], groups[5], groups[7]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

for groups in email_regex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
