import click
import sys
from typing import List


@click.command()
@click.argument('input', default='software/README.md', type=click.File())
@click.pass_context
def mutate(ctx, input):
    with sys.stdout as output:
        for line in input:
            try:
                # not a table, just copy
                if line[0] != '|':
                    output.write(line)
                    continue
                # initial status table, just copy
                if line.count('|') == 3:
                    output.write(line)
                    continue
                # table header, add header fields
                if '| Supplier' in line:
                    output.write(mutate_header(line))
                    continue
                # table underline, add header fields
                if '|:----' in line:
                    output.write(mutate_underline(line))
                    continue

                # table line, add cells
                output.write(mutate_record(line))
            except ValueError as e:
                print("\nOffending line:", file=sys.stderr)
                print(line, file=sys.stderr)
                raise e


def mutate_header(line) -> str:
    cve4104 = ' Status CVE-2021-4104 '
    cve45046 = ' Status CVE-2021-45046 '
    cve44228 = ' Status CVE-2021-44228 '

    _, vendor, product, version, status, comment, link, _ = line.split('|')

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, comment, link]))


def mutate_underline(line) -> str:
    cve4104 = ':--------------------:'
    cve45046 = ':---------------------:'
    cve44228 = ':---------------------:'

    _, vendor, product, version, status, comment, link, _ = line.split('|')

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, comment, link]))


def mutate_record(line) -> str:
    cve4104 = ' '
    cve45046 = ' '
    _, vendor, product, version, status, comment, link, _ = line.split('|')
    cve44228 = ' '+status.strip()+' '

    if 'Fix' in cve44228:
        cve4104 = ' Not vuln '

    if 'Not vuln' in cve44228:
        cve4104 = ' Not vuln '
        cve45046 = ' Not vuln '

    if 'Workaround' in cve44228:
        cve4104 = ' Not vuln '

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, comment, link]))


def table_line(fields: List[str]) -> str:
    return("|"+"|".join(fields)+"|\n")


if __name__ == '__main__':
    mutate(obj={})
