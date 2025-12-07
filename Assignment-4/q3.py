import re

def normalize_phones(s):
    pattern = re.compile(
        r'(\+91|0091|\(91\)|91)\s*([0-9][0-9\s-]{8}[0-9])'
    )

    def repl(m):
        digits = re.sub(r'\D', '', m.group(2))
        return f"+91-{digits}"

    return pattern.sub(repl, s)
inp = "Contact: +91-9876543210, Office: (91) 98765 43210, Home: 0091 9876543210"
print(normalize_phones(inp))