import re

def extract_date_parts(s):
    pattern = r'(\d{2})-(\d{2})-(\d{4})'
    m = re.search(pattern, s)

    if m:
        return (
            m.group(0),   # whole match
            m.group(1),   # day
            m.group(2),   # month
            m.group(3),   # year
            m.span(),     # (start, end)
            m.lastindex   # should be 3
        )
    return None
s = "Backup 05-11-2025 complete"
print(extract_date_parts(s))