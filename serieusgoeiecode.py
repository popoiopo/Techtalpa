#import python skills
# cat file.txt | python script.py |
import fileinput
import sys

for line in sys.stdin:

    # split line on space starting the 3rd line
    splitline = line.split()
    print splitline