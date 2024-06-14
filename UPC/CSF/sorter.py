# Read the FQCSF.md, split by \n##, sort by the first line of each section and write to a new file
# Usage: python sorter.py FQCSF.md sorted.md
# import sys

# source=sys.argv[1]
# target=sys.argv[2]

source = "FQCSF.md"
target = "sorted.md"

with open(source, "r", encoding="utf-8") as f:
    text = "\n"+f.read()

sections = text.split("\n## ")
sections = [section.strip() for section in sections]

sorted_sections = sorted(sections)#, key=lambda x: x.split("\n")[0])
print(len(sorted_sections))
with open(target, "w", encoding="utf-8") as f:
    f.write(("\n## ".join(sorted_sections))[1:])
