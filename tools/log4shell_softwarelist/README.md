# Log4shell software list tool

This directory contains info for the softwarelist parser tool. This script parsers the Software list markdown table and can export it to CSV or JSON format.

## Installation

1. Install Python3
2. Install pip
3. Install the Python dependencies via pip

```bash
pip install -r requirements.txt
```

## Usage

From within this directory execute the following:

```bash
# To parse softwarelist to CSV use
python softwarelist_parser.py csv

# To parse softwarelist to json use
python softwarelist_parser.py json

# To write to a file, append to end of CLI; e.g.:
python softwarelist_parser.py csv output.csv
python softwarelist_parser.py json output.json
```
