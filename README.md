# Log4j Vulnerability (CVE-2021-44228)

This repo contains operational information regarding the vulnerability in the Log4j logging library (CVE-2021-44228). For additional information see:

* [NCSC-NL advisory](https://www.ncsc.nl/actueel/advisory?id=NCSC-2021-1052)
* [MITRE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228)

## Repository contents

| Directory  | Purpose |
|:-----------|:--------|
| iocs       | Contains any Indicators of Compromise, such as scanning IPs, etc |
| mitigation | Contains info regarding mitigation, such as regexes for detecting scanning activity and more |
| scanning   | Contains references to methods and tooling used for scanning for the Log4j vulnerability |
| software   | Contains a list of known vulnerable and not vulnerable software |

**Please note that these directories are not complete, and are currently being expanded.**

**NCSC-NL has published a HIGH/HIGH advisory for the Log4j vulnerability. Normally we would update the HIGH/HIGH advisory for vulnerable software packages, however due to the extensive amounts of expected updates we have created a list of known vulnerable software in the software directory.**

## Pull request welcome

If you have any additional information to share relevant to the Log4j vulnerability, please feel free to open a Pull request.
