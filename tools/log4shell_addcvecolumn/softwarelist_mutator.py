import csv as py_csv
import sys
import json as py_json
import pathlib
import re
import tempfile

from typing import List

import click
import unicodedata

line_re = re.compile('(\|[^|]+\|[^|]+\|[^|]+\|)([^|]+)(\|.*)')

HEADERS = [
    'Supplier',
    'Product',
    'Version',
    'Status',
    'Notes',
    'Links'
]

@click.command()
@click.option('--path', default='../../software/README.md', help='Path to software list README.md', type=click.File())
@click.argument('output', default='-', type=click.File('w+'))
@click.pass_context
def mutate(ctx, path, output):
    for line in path:
        if line[0] != '|':
            print(line, file=output)
            continue
        if line.count('|') == 3:
            print(line, file=output)
            continue # status table
        if '| Supplier' in line:
            print(mutate_header(line), file=output)
            continue # table header
        if '|:----' in line:
            print(mutate_underline(line), file=output)
            continue # table underline

        print(mutate_record(line), file=output)

def mutate_header(line):
    cve4104 = ' Status CVE-2021-4104 '
    cve45046 = ' Status CVE-2021-45046 '
    cve44228 =' Status CVE-2021-44228 '

    _, vendor, product, version, status, comment, link, _ = line.split('|')

    return('|'+'|'.join([vendor, product, version, cve4104, cve44228, cve45046, comment, link])+'|')

def mutate_underline(line):
    cve4104 = ':--------------------:'
    cve45046 = ':---------------------:'
    cve44228 =':---------------------:'

    _, vendor, product, version, status, comment, link, _ = line.split('|')

    return('|'+'|'.join([vendor, product, version, cve4104, cve44228, cve45046, comment, link])+'|')

def mutate_record(line):
    cve4104 = ' '
    cve45046 = ' '
    _, vendor, product, version, status, comment, link, _ = line.split('|')
    cve44228 = status

    if 'Not vuln' in cve44228:
        cve4104 = ' Not Vuln '
        cve45046 = ' Not Vuln '

    return('|'+'|'.join([vendor, product, version, cve4104, cve44228, cve45046, comment, link])+'|')

if __name__ == '__main__':
    mutate(obj={})