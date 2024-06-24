import sys

# Index 0 would be the name of the file (name.py)
"""print("hello, my name is", sys.argv[0])"""

# Index 1 is the first name I provide when I write "python name.py David" - in this case it'll be David
"""print("hello, my name is", sys.argv[1])"""

# The way we did it below, avoids the need to handle try - exceptions (IndexValue exception in this case)
# If I'd like to support full name I can add "" to the CLI, e.g. python name.py "David Malan"
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Introducing slice. sys.argv[1:] will give me a slice of the list, in this case, starting at index 1.
# I could also request a slice sys.argv[1:-1] which would give me the results in index 1 up to the one before the last.
for arg in sys.argv:
    print("hello, my name is", arg)