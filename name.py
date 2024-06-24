import sys

# Index 0 would be the name of the file (name.py)
"""print("hello, my name is", sys.argv[0])"""

# Index 1 is the first name I provide when I write "python name.py David" - in this case it'll be David
"""print("hello, my name is", sys.argv[1])"""

# The way we did it below, avoids the need to handle try - exceptions (IndexValue exception in this case)
# If I'd like to support full name I can add "" to the CLI, e.g. python name.py "David Malan"
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])