import re

text = "Random <tag>first</tag> some text <tag>second</tag> end"

# (a) Greedy: match from first <tag> to LAST </tag>
m = re.search(r'<tag>.*</tag>', text)
print("Greedy match:")
print(m.group(), "\n")

# (b) Non-greedy: match EACH tag pair separately
matches = re.findall(r'<tag>.*?</tag>', text)
print("Non-greedy matches:")
for i, item in enumerate(matches, 1):
    print(f"{i}: {item}")