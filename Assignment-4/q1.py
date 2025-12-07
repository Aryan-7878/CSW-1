import re

def filter_emails(lst):
    pattern = r'^[A-Za-z0-9][A-Za-z0-9._]*@[A-Za-z]+\.[A-Za-z]{2,4}$'
    valid_emails = []

    for email in lst:
        if re.match(pattern, email):
            valid_emails.append(email)

    return valid_emails
lst = [
    "student123@gmail.com",
    "teacher.name@soa.edu",
    "abc.xyz@abc.in",
    "xyz#12@abc.com",
    "bad@1n.com"
]

print(filter_emails(lst))