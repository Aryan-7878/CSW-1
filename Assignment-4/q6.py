import re

pattern = r'^[a-z]+[0-9]+$'

tests = ["abc123", "a1b2", "ABC123", "hello99", "test", "99abc"]

for t in tests:
    if re.match(pattern, t):
        print(t, "→ pass")
    else:
        print(t, "→ fail")