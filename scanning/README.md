# Log4j overview Scanning software

This page contains an overview of any scanning software regarding the Log4j vulnerability. 

**NCSC-NL has not verified the scanning software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide scanning software from reliable sources.**

## Vulnerability Detection
Checks if the application is vulnerable to CVE-2021-44228.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| Canary Tokens |  Log4Shell Vulnerability Tester | https://canarytokens.org/generate |
| CrowdStrike  | Free Targeted Log4j Search Tool | https://www.crowdstrike.com/blog/free-targeted-log4j-search-tool/ |
| crypt0jan     | Perform a scan of a single host (using Powershell) to see if it's vulnerable | https://github.com/crypt0jan/log4j-powershell-checker |
| Diverto | Nmap NSE scripts to check against log4shell | https://github.com/Diverto/nse-log4shell |
| Dtact | DIVD-2021-00038 log4j scanner Scan paths including archives for vulnerable log4 | https://github.com/dtact/divd-2021-00038--log4j-scanner |
| Deepfence ThreatMapper | Apache v2, powerful runtime vulnerability scanner for kubernetes, virtual machines and serverless | https://github.com/deepfence/ThreatMapper |
| FullHunt | Open detection and scanning tool (Python) for discovering and fuzzing for Log4J vulnerability | https://github.com/fullhunt/log4j-scan |
| Fox-IT | A script to scan the filesystem to find Log4j2 that is vulnerable to Log4Shell (CVE-2021-44228) (Python)| https://github.com/fox-it/log4j-finder |
| Grype   | Open source vulnerability scanner (docker), picks up nested JARs containing log4j | https://github.com/anchore/grype |
| Huntress  | Online Log4Shell Vulnerability Tester| https://log4shell.huntress.com/ |
| logpresso | Scans for java files that are vulnerable and may rename it for mitigation | https://github.com/logpresso/CVE-2021-44228-Scanner |
| Logout4shell | Exploits the log4shell vulnerability in order to vaccinate the vulnerable target | https://github.com/Cybereason/Logout4Shell |
| Northwave Security | Northwave Log4j CVE-2021-44228 checker (python) | https://github.com/NorthwaveSecurity/log4jcheck |
| Northwave Security | Northwave Log4j CVE-2021-44228 checker Powershell version | https://github.com/crypt0jan/log4j-powershell-checker |
| OlafHaalstra | Scans a list of URLs with `GET` or `POST` request with user defined parameters (python) | https://github.com/OlafHaalstra/log4jcheck |
| ProferoSec | Scans network or IP address for Log4j vulnerability by making callback to scanning host | https://github.com/proferosec/log4jScanner |
| Qualys | Local scanner to check for CVE-2021-4104, CVE-2021-44228, CVE-2021-45046 and CVE-2021-45105 | https://github.com/Qualys/log4jscanwin
| righel |  Nmap NSE script to inject jndi payloads with customizable templates into HTTP targets | https://github.com/righel/log4shell_nse |
| silentsignal | Log4Shell scanner for Burp Suite | https://github.com/silentsignal/burp-log4shell |
| Trendmicro | Online Log4j tester Trendmicro | https://log4j-tester.trendmicro.com/ |


## Log4j2 Detection

### How to find
- Java applications are distributed in Java ARchives, also known as JAR files. JAR files contain, among other things, compiled Java code in .class files.
- The file that contains the Log4shell vulnerability (CVE-2021-44228) is: `JndiLookup.class` which is part of the `log4j-core` library.
- There are three commonly used extensions for Java Archives: jar, war and ear. Each Java archive may contain nested archives. 
  For example:
  - `ear` files often contain jar and war files
  - `war` files often contain jar files
  - `jar` files may contain other jar files
- In order to find the vulnerable 'JndiLookup.class' file and by extension the log4j-core library, each found Java archive must be recursively scanned; meaning that nested Java archives must also be scanned.


### Links
Checks if the application or system is using Log4j2.
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| 1lann  | Scans a file or folder recursively for jar files that may be vulnerable | https://github.com/1lann/log4shelldetect |
| Aholzel | Splunk query's to detect the used Log4j version and detect abuse | https://github.com/aholzel/log4j_splunk_querys |
| Crowdstrike CAST | Quick scanner to walk filesystems looking for vulnerable versions of log4j (powershell) | https://github.com/CrowdStrike/CAST |
| Devotech[^1] | Powershell: Queries domain servers and scans for log4j-core files. (slow) | https://github.com/devotech/check-log4j |
| DIVD | This scanner will recursively scan paths including archives for vulnerable log4j versions and JndiLookup.class files. |https://github.com/dtact/divd-2021-00038--log4j-scanner |
| Forescout | Samples of exploit attempts; The evolving Log4Shell story: analysis of ongoing and future exploits | https://github.com/Forescout/log4j_response |
| GoHoyer[^2] | Bash script to detect vulnerable log4j-2 jar files | https://gist.github.com/gohoyer/9a40d8e0e46c4c78c99cc9d5e9adc5aa |
| JFrog | Detects files containing vulnerable Log4j versions and also scans for locations in code where log4j 2 is called. | https://github.com/jfrog/log4j-tools |
| Kelvin Tegelaar[^3] | Open sourced(MIT license) PowerShell log4j detection. Uses "Everything" to prevent high system load | https://www.cyberdrain.com/monitoring-with-powershell-detecting-log4j-files/ |
| Mergebase | Detects vulnerable Log4J versions on your file-system. It is able to find instances that are hidden several layers deep. Linux/Windows/Mac | https://github.com/mergebase/log4j-detector |
| NCCgroup  | Version hashes (MD5, SHA1 and SHA256) for log4j2 versions| https://github.com/nccgroup/Cyber-Defence/tree/master/Intelligence/CVE-2021-44228 |
| Neo23x0[^4]   | Florian Roth Log4j2 detection script | https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b |
| sp4ir[^5]     | Powershell script to detect Log4Shell| https://github.com/sp4ir/incidentresponse/blob/35a2faae8512884bcd753f0de3fa1adc6ec326ed/Get-Log4shellVuln.ps1 |
| Syft | Open source SBOM scanner, can detect all dependencies including log4j | https://github.com/anchore/syft/ |
| yannart | Open sourced(MIT license) scanner to analyze recursively for jar and other Java archives that may be vulnerable (written in Rust) | https://github.com/yannart/log4shell-scanner-rs |

[^1]: Only scans filenames, does not search for vulnerable JndiLookup.class, does not scan nested Java archives, does not scan .war and .ear files.
[^2]: Only scans filenames, does not scan nested Java archives, does not scan .war and .ear files.
[^3]: Does not scan nested Java archives, does not scan .war and .ear files.
[^4]: Windows and Linux scripts are limited and do not scan nested java archives.
[^5]: Only scans filenames, does not scan nested Java archives, does not scan .war and .ear files.
