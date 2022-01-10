# Log4shell software list mutation tool

This directory contains scripts to add additional columns to the software list. This script parses the Software list markdown table and splits out the status column for additional CVEs.

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
cd software/
# To mutate the software list
for file in `ls software_list_*.md`; do python <scriptname>.py $file > /tmp/$file; mv /tmp/$file $file; done

# review changes
git diff

# commit changes
git add software_list_*.py
git commit
```
