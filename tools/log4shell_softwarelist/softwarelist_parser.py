import sys
import csv as py_csv
import json as py_json

from pathlib import Path
from typing import List, Iterator

import click
import mistune
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
    link_index = len(HEADERS) - 1

    for index, header in enumerate(HEADERS):
        # Parse links differently
        if index == link_index:
            if len(record) == link_index:
                result[header] = {}
            else:
                result[header] = parse_links(record[index].find_all('a'))

        else:
            # Ensure unicode in text is properly parsed
            result[header] = unicodedata.normalize("NFKD", record[index].text)

    return result

def parse_software_file(path: Path) -> Iterator[dict]:
    """ Parse a single software list file

    :param path: path of file to parse
    :yield: a single parse record from file
    """

    # Parse Markdown to HTML and get soup
    with path.open('r') as f:
        content = f.read()

    html = mistune.html(content)
    soup = BeautifulSoup(html, 'html.parser')

    # Look for all tr columns with td fields, after first h3 header
    for row in soup.find_all('tr'):
        tds = row.find_all('td')

        if tds:  # ensure empty tr are ignored
            yield parse_record(tds)

@click.group()
@click.option('--path', default='../../software/', help='Path to software list', type=click.Path(exists=True, path_type=Path))
@click.pass_context
def main(ctx, path):
    records = list()

    # Get list of software list files
    software_lists = sorted(f for f in path.iterdir() if 'software_list_' in f.name)

    for software_file in software_lists:
        file_records = [r for r in parse_software_file(software_file)]
        records += file_records

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
