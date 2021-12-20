import argparse
import sys
import json

output = []

parser = argparse.ArgumentParser(description="Convert NCSC-NL/log4shell Markdown table to JSON. (alexandre.dulaunoy@circl.lu")
parser.add_argument('-f', help="Markdown file to convert")
args = parser.parse_args()

found_header = False
if args.f is None:
    parser.print_help()
    sys.exit()
else:
    table = open(args.f).read()
for n, line in enumerate(table[1:-1].split('\n')):
    data = {}
    if not line.startswith('|'):
        continue
    if line.startswith('| Supplier'):
        header = [t.strip() for t in line.split('|')[1:-1]]
        found_header = True
    if found_header:
        values = [t.strip() for t in line.split('|')[1:-1]]
        for col, value in zip(header, values):
            data[col] = value
        output.append(data)

print(json.dumps(output))
