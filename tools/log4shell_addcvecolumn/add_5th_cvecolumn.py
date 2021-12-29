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
    cveXXXXX = ' Status CVE-2021-XXXXX '

    _, vendor, product, version, cve4104, cve44228, cve45046, cve45105, comment, link, _ = line.split('|')

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, cve45105, cveXXXXX, comment, link]))


def mutate_underline(line) -> str:
    cveXXXXX = ':---------------------:'

    _, vendor, product, version, cve4104, cve44228, cve45046, cve45105, comment, link, _ = line.split('|')

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, cve45105, cveXXXXX, comment, link]))


def mutate_record(line) -> str:
    cveXXXXX = ' '
    _, vendor, product, version, cve4104, cve44228, cve45046, cve45105, comment, link, _ = line.split('|')

    # Log4j 1.x is not impacted by CVE-2021-XXXXX
    if ('Fix' in cve4104 or 'Vulnerable' in cve4104) and 'Not vuln' in cve44228:
        cveXXXXX = 'Not vuln'

    # Software not using Log4j is not impacted by CVE-2021-XXXXX
    if 'Not vuln' in cve4104 and 'Not vuln' in cve44228 and 'Not vuln' in cve45046 and 'Not vuln' in cve45105:
        cveXXXXX = 'Not vuln'

    return(table_line([vendor, product, version, cve4104, cve44228, cve45046, cve45105, cveXXXXX, comment, link]))


def table_line(fields: List[str]) -> str:
    return("|"+"|".join(fields)+"|\n")


if __name__ == '__main__':
    mutate(obj={})
