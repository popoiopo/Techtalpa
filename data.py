# import python skills
# cat file.txt | python script.py |
import sys
lijst = []
for line in sys.stdin:

    # split line on space starting the 3rd line
    lijst.append(line.split())
print lijst[0]