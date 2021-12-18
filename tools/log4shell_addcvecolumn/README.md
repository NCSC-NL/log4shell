# Log4shell software list mutation tool

This directory contains a script to add additional columns to the software list. This script parses the Software list markdown table and splits out the status column for additional CVEs.

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
# To mutate the software list
python softwarelist_mutator.py software/README.mdown > /tmp/README.mdown

# show differences
diff -y -M200 software/README.mdown /tmp/README.mdown

# move in place
mv /tmp/README.mdown software/README.mdown

# commit change
git add software/README.mdown
git commit
```
