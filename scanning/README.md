# Log4j overview Scanning software

This page contains an overview of any scanning software regarding the Log4j vulnerability. 

**NCSC-NL has not verified the scanning software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide scanning software from reliable sources.**

## Vulnerability Detection
Checks if the application is vulnerable to CVE-2021-44228.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| crypt0jan     | Perform a scan of a single host (using Powershell) to see if it's vulnerable | https://github.com/crypt0jan/log4j-powershell-checker |
| Huntress  | Online Log4Shell Vulnerability Tester| https://log4shell.huntress.com/ |
| Canary Tokens |  Log4Shell Vulnerability Tester | https://canarytokens.org/generate |
| Diverto | Nmap NSE scripts to check against log4shell | https://github.com/Diverto/nse-log4shell |
| righel |  Nmap NSE script to inject jndi payloads with customizable templates into HTTP targets | https://github.com/righel/log4shell_nse |
| silentsignal | Log4Shell scanner for Burp Suite | https://github.com/silentsignal/burp-log4shell |
| Northwave Security | Northwave Log4j CVE-2021-44228 checker | https://github.com/NorthwaveSecurity/log4jcheck |
| Northwave Security | Northwave Log4j CVE-2021-44228 checker Powershell version | https://github.com/crypt0jan/log4j-powershell-checker |
| OlafHaalstra | Scans a list of URLs with `GET` or `POST` request with user defined parameters | https://github.com/OlafHaalstra/log4jcheck |
| Grype   | Open source vulnerability scanner (docker), picks up nested JARs containing log4j | https://github.com/anchore/grype |
| logpresso | Scans for java files that are vulnerable and may rename it for mitigation | https://github.com/logpresso/CVE-2021-44228-Scanner |
| FullHunt | Open detection and scanning tool (Python) for discovering and fuzzing for Log4J vulnerability | https://github.com/fullhunt/log4j-scan |
| Dtact | DIVD-2021-00038 log4j scanner Scan paths including archives for vulnerable log4 | https://github.com/dtact/divd-2021-00038--log4j-scanner |
| ThreatMapper | Runtime log4j2 exploitablity scanner with attack path visualization and mitigation for hosts and k8s | https://github.com/deepfence/ThreatMapper |


## Log4j2 Detection
Checks if the application or system is using Log4j2.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| Neo23x0   | Florian Roth Log4j2 detection script | https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b |
| sp4ir     | Powershell script to detect Log4Shell| https://github.com/sp4ir/incidentresponse/blob/35a2faae8512884bcd753f0de3fa1adc6ec326ed/Get-Log4shellVuln.ps1 |
| NCCgroup  | Version hashes (MD5, SHA1 and SHA256) for log4j2 versions| https://github.com/nccgroup/Cyber-Defence/tree/master/Intelligence/CVE-2021-44228 |
| 1lann  | Scans a file or folder recursively for jar files that may be vulnerable | https://github.com/1lann/log4shelldetect |
| Syft | Open source SBOM scanner, can detect all dependencies including log4j | https://github.com/anchore/syft/ |
| Devotech | Powershell: Queries domain servers and scans for log4j-core files. (slow) | https://github.com/devotech/check-log4j |
