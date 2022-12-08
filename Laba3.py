import re

with open("data.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        if re.search(r"z.{3}z", line) is not None:
            print(line)
