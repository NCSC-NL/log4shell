# Log4j overview Scanning software

This page contains an overview of any scanning software regarding the Log4j vulnerability. 

**NCSC-NL has not verified the scanning software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide scanning software from reliable sources.**

## Vulnerability Detection
Checks if the application is vulnerable to CVE-2021-44228.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| crypt0jan     | Perform a scan of a single host (using Powershell) to see if it's vulnerable | [source](https://github.com/crypt0jan/log4j-powershell-checker) |
| Northwave Log4j checker | Scans specified url with a `GET` with payload in url or *User Agent* | [source](https://github.com/NorthwaveSecurity/log4jcheck) |
| log4jcheck | Scans a list of URLs with `GET` or `POST` request in combination with user defined parameters | [source](https://github.com/OlafHaalstra/log4jcheck) |
| log4j_rce_check | Scans specified host with payload in the *User Agent* | [source](https://gist.github.com/byt3bl33d3r/46661bc206d323e6770907d259e009b6) |
| Canary Tokens | Amongst other a Log4Shell JNDI string with URL can be generated for which the DNS queries are logged and presented in an overview with caller information. | [source](https://canarytokens.org/generate) |
| Huntress  | Online Log4Shell Vulnerability Tester| [source](https://log4shell.huntress.com/) |
|  Diverto | Nmap NSE scripts to check against log4shell | [source](https://github.com/Diverto/nse-log4shell) |

## Log4j2 Detection
Checks if the application or system is using Log4j2.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| Neo23x0   | Florian Roth Log4j2 detection script | [source](https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b) |
| sp4ir     | Powershell script to detect Log4Shell| [source](https://github.com/sp4ir/incidentresponse/blob/35a2faae8512884bcd753f0de3fa1adc6ec326ed/Get-Log4shellVuln.ps1) |
| NCCgroup  | Version hashes (MD5, SHA1 and SHA256) for log4j2 versions| [source](https://github.com/nccgroup/Cyber-Defence/tree/master/Intelligence/CVE-2021-44228) |
