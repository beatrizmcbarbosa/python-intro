import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
# With argparse, arguments can be passed in the cli in no particular order
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
