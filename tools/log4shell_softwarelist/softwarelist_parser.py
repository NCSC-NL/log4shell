import csv as py_csv
import sys
import json as py_json
import pathlib
import tempfile

from typing import List

import click
import mistune
import requests
import unicodedata

from bs4 import BeautifulSoup
from bs4.element import Tag

HEADERS = [
    'Supplier',
    'Product',
    'Version',
    'Status CVE-2021-4104',
    'Status CVE-2021-44228',
    'Status CVE-2021-45046',
    'Status CVE-2021-45105',
    'Notes',
    'Links'
]

def download_softwarelist() -> str:
    """ Download softwarelist to parse

    :return: Markdown content of software list
    """
    url = "https://raw.githubusercontent.com/NCSC-NL/log4shell/main/software/README.md"
    response = requests.get(url)
    return response.content

def parse_links(links: List[Tag] = None) -> dict:
    """ Get all links info from Links column

    :return: Dictionary with `{link_text: link_href}`
    """
    return {link.text: link.get('href') for link in links}

def parse_record(record: List[Tag] = None) -> dict:
    """ Parse single tr record in Software list

    :return: Dictionary of parsed cell from record
    """

    result = dict()

    for index, header in enumerate(HEADERS):
        # Parse links differently
        if index == 8:
            if len(record) == 8:
                result[header] = {}
            else:
                result[header] = parse_links(record[index].find_all('a'))

        else:
            # Ensure unicode in text is properly parsed
            result[header] = unicodedata.normalize("NFKD", record[index].text)

    return result

@click.group()
@click.option('--path', default='../../software/README.md', help='Path to software list README.md', type=click.File())
@click.pass_context
def main(ctx, path):

    # Parse Markdown to HTML and get soup
    content = path.read()
    html = mistune.html(content)
    soup = BeautifulSoup(html, 'html.parser')

    # Look for all tr columns with td fields, after first h3 header
    records = list()
    first_h3 = soup.find('h3')

    for x in first_h3.next_elements:
        if isinstance(x, Tag) and x.name == 'tr':
            tds = x.find_all('td')

            if tds:  # ensure empty tr are ignored
                records.append(parse_record(tds))

    ctx.obj['records'] = records


@main.command()
@click.argument('output', default='-', type=click.File('w+'))
@click.pass_context
def json(ctx, output):
    py_json.dump(ctx.obj['records'], output)

@main.command()
@click.argument('output', default='-', type=click.File('w+'))
@click.pass_context
def csv(ctx, output):
    writer = py_csv.DictWriter(output, HEADERS)

    writer.writeheader()

    # cleanup links
    for record in ctx.obj['records']:
        record['Links'] = list(record['Links'].values())
        writer.writerow(record)


if __name__ == '__main__':
    main(obj={})
