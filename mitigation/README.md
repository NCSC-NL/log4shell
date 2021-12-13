# Log4j overview Detection rules and software

This page contains an overview of any detection software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known rules to detect Log4j presence or (suspected) Exploitation. Futhermore any references will contain specific information regarding detection.

**NCSC-NL has not verified the rules and detection software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide rules and detection software from reliable sources.**

## Detection Regex

Overall detection regex

```plain
(\$|%24)(\{|%37B).*j.*n.*d.*i.*(:|%3A).+
```

## Closed source intelligence

| Supplier        | Product         | Links / Rule|
|:----------------|:----------------|:---------------:|
| Akamai       | Cloud | `sudo egrep -i -r "\$\{jndi:(ldap[s]?|rmi|dns)://' /var/log` |
| Cloudflare   | Cloud | [source](https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/) |
| Google       | Cloud | [source](https://cloud.google.com/blog/products/identity-security/cloud-armor-waf-rule-to-help-address-apache-log4j-vulnerability)|
| Palo Alto Networks   | Prisma Cloud | [source](https://unit42.paloaltonetworks.com/apache-log4j-vulnerability-cve-2021-44228/) |
| Palo Alto networks   | Firewall | Threat ID 91991 ingested after content update 8498 |
| Microsoft    | Defender | [source](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/) |
| Microsoft    | Sentinel| [source](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/) |
| Tanium   | Tanium | [source](https://community.tanium.com/s/article/How-Tanium-Can-Help-with-CVE-2021-44228-Log4Shell) |
| Trend Micro   | Cloud One| LI Rule 1011241 |
| Tenable  | Nesus | [source](https://www.tenable.com/plugins/search?q=cves%3A%28%22CVE-2021-44228%22%29&sort=&page=1) |
| RSA  | Netwitness | client.all contains "${j" || client.all contains "${J" |
| Northwave Security | Not specific | [source](https://github.com/NorthwaveSecurity/log4jcheck) |
| Northwave Security | Not specific | [source](https://github.com/crypt0jan/log4j-powershell-checker) |
| Splunk | Splunk | [source](https://www.splunk.com/en_us/blog/security/log-jammin-log4j-2-rce.html) |
| Qualys  | Cloud Platform | [source](https://blog.qualys.com/vulnerabilities-threat-research/2021/12/10/apache-log4j2-zero-day-exploited-in-the-wild-log4shell) |

## Opensource Intelligence


### Network based detection
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
|  Diverto | Nmap NSE scripts to check against log4shell | [source](https://github.com/Diverto/nse-log4shell) |
|  NCC Group | Log4Shell: Reconnaissance and post exploitation network detection | [source](https://research.nccgroup.com/2021/12/12/log4shell-reconnaissance-and-post-exploitation-network-detection/) |

Snort and Suricata rules:

| Note             | Rule-range        | Rule |
|:----------------|:----------------|:---------------:|
| These are ET Open free community detections to alert on current exploit activity.  | SID range 2034647-2034652. | [source](https://rules.emergingthreatspro.com/open/) |



### Host based detection

| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| Neo23x0   | Florian Roth Grep and YARA rule for log4j2 exploitation | [source](https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b) |
| Neo23x0   | Florian Roth Log4j2 detection script | [source](https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b) |
| Neo23x0   | Florian Roth Detects exploitation attempt against log4j RCE vulnerability fields (Sigma rule) | [source](https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j_fields.yml) |
| Neo23x0   | Florian Roth Detects exploitation attempt against log4j RCE vulnerability (Sigma rule) | [source](https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j.yml) |
| sp4ir     | Powershell script to detect Log4Shell| [source](https://github.com/sp4ir/incidentresponse/blob/35a2faae8512884bcd753f0de3fa1adc6ec326ed/Get-Log4shellVuln.ps1) |
| crypt0jan     | Perform a scan of a single host (using Powershell) to see if it's vulnerable | [source](https://github.com/crypt0jan/log4j-powershell-checker) |
| NCCgroup  | Version hashes (MD5, SHA1 and SHA256) for log4j2 versions| [source](https://github.com/nccgroup/Cyber-Defence/tree/master/Intelligence/CVE-2021-44228) |
| Huntress  | Online Log4Shell Vulnerability Tester| [source](https://log4shell.huntress.com/) |
