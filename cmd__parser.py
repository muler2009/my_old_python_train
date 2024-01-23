import argparse

parser = argparse.ArgumentParser(
    description="a Program to Test Command line Interface"
)

parser.add_argument("-n", "--name", help="Put the name of arguments", required=True, metavar="")
parser.add_argument("-v", "--version", help="version of the program", required=False, metavar="")

args = parser.parse_args()
msg = f"Hello {args.name} Version is {args.version}"
print(msg)