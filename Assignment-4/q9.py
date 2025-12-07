import re

def find_upper_before_digit(s):
    # Capture the uppercase letter, then allow anything, then require a digit
    pattern = r'([A-Z]).*\d'

    m = re.search(pattern, s)
    if m:
        return (m.group(1), m.start(1))   # return the uppercase letter + its index
    return None
print(find_upper_before_digit("a B blah 9"))