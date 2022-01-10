# log4shell-markdown-to-json

A [minimal script to convert log4shell markdown](./log4shell-markdown-to-json.py) tables into a single JSON dictionary. The script doesn't need any external dependencies beside the standard Python 3 libraries.

# Usage

`python3 log4shell-markdown-to-json.py -f ../../software/README.md | jq .`
