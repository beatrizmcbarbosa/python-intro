"""import cowsay"""
import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# Cow saying with Trex option
"""if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])"""

# Cow option
"""if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])"""