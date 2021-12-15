# Log4j Vulnerability (CVE-2021-44228)

This repo contains operational information regarding the vulnerability in the Log4j logging library (CVE-2021-44228). For additional information see:

* [NCSC-NL advisory](https://www.ncsc.nl/actueel/advisory?id=NCSC-2021-1052)
* [MITRE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228)

## Repository contents

| Directory                          | Purpose |
|:-----------------------------------|:--------|
| [hunting](hunting/README.md)       | Contains info regarding hunting for exploitation |
| [iocs](iocs/README.md)             | Contains any Indicators of Compromise, such as scanning IPs, etc |
| [mitigation](mitigation/README.md) | Contains info regarding mitigation, such as regexes for detecting scanning activity and more |
| [scanning](scanning/README.md)     | Contains references to methods and tooling used for scanning for the Log4j vulnerability |
| [software](software/README.md)     | Contains a list of known vulnerable and not vulnerable software |

**Please note that these directories are not complete, and are currently being expanded.**

**NCSC-NL has published a HIGH/HIGH advisory for the Log4j vulnerability. Normally we would update the HIGH/HIGH advisory for vulnerable software packages, however due to the extensive amounts of expected updates we have created a list of known vulnerable software in the software directory.**

## Contributions welcome

If you have any additional information to share relevant to the Log4j vulnerability, please feel free to open a Pull request. New to this? [Read how to contribute in GitHub's documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository).

### Thank you

Dear contributors, partners all over the world,

We have received an impressive/enormous number of pull requests on this repo. It contains vital information that contributes to the situational overview around the Log4j vulnerability. The list of vulnerable applications is currently one of the most up-to-date ones with continuous input from across the globe. It is still expanding and we are working hard to process all the contributions. 

Due to our joint efforts and strong cooperation we are confident that we will be better equipped to manage this situation.

Thank you all very much for your hard work and we keep welcoming your input via GitHub. 
