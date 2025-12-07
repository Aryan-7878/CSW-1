import re

def verify_passwd(s):
    # Rule 1: At least 8 characters
    rule1 = re.search(r'.{8,}', s)

    # Rule 2: Contains ONLY allowed characters (letters, digits, @#$%^&*!)
    rule2 = re.fullmatch(r'[A-Za-z0-9@#$%^&*!]+', s)

    # Rule 3: At least one digit
    rule3 = re.search(r'\d', s)

    # Rule 4: At least one letter
    rule4 = re.search(r'[A-Za-z]', s)

    # Rule 5: At least one special character
    rule5 = re.search(r'[@#$%^&*!]', s)

    return bool(rule1 and rule2 and rule3 and rule4 and rule5)
passwords = [
    "abc123",           # too short
    "Abcdefgh",         # no digit, no special
    "abcd1234",         # no special char
    "abcd@123",         # valid
    "ABC123!!",         # valid
    "abc$12",           # too short
    "12345678!",        # no letter
]

for p in passwords:
    print(p, "-", verify_passwd(p))