# Log4j overview IoCs

This page contains an overview of any Indicators of Compromise regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known IOCs which can be used to detect and block. Furthermore any references will contain specific information regarding indicator reports.

**NCSC-NL has not verified the IoCs listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide IoCs from reliable sources.**

## Network related IoC's
| Note     | Links |
|:----------------|:----------------|
| The list of callback servers, updated by Greynoise  | https://gist.github.com/superducktoes/9b742f7b44c71b4a0d19790228ce85d8 |
| The list of scanning IP's, updated by Greynoise  | https://gist.github.com/gnremy/c546c7911d5f876f263309d7161a7217 |
| Threatfox  | https://threatfox.abuse.ch/browse/tag/log4j/ |
| UrlHaus  | https://urlhaus.abuse.ch/browse/tag/log4j/ |
| Malware Bazaar | https://bazaar.abuse.ch/browse/tag/log4j/ |
| CTCI | https://docs.google.com/spreadsheets/d/e/2PACX-1vT1hFu_VlZazvc_xsNvXK2GJbPBCDvhgjfCTbNHJoP6ySFu05sIN09neV73tr-oYm8lo42qI_Y0whNB/pubhtml# |
| Malwar3Ninja | https://twitter.com/bad_packets/status/1469225135504650240|
| GovCert.ch | https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/|
| isc.sans.edu | https://isc.sans.edu/diary/Log4Shell+exploited+to+implant+coin+miners/28124 |
| isc.sans.edu (2) | https://isc.sans.edu/diary/rss/28172 |
| cert-agid.gov.it (Contains scan IP's) | https://cert-agid.gov.it/download/log4shell-iocs.txt |
| jamesspi (Contains scan IP's) | https://log4shell.threatsearch.io/ |
| Nozomi Networks | https://www.nozominetworks.com/blog/critical-log4shell-apache-log4j-zero-day-attack-analysis/ |
| NLD Police | https://thanksforallthefish.nl/log4j_hashes.txt (Thor format) Auto Updated every 15min |
| NLD Police | https://thanksforallthefish.nl/log4j_hashes_sha256.txt (line-by-line)  Auto Updated every 15min |
| NLD Police | https://thanksforallthefish.nl/log4j_hashes_sha1md5.txt (line-by-line)  Auto Updated every 15min |
| NLD Police | https://thanksforallthefish.nl/log4j_domains.txt (Thor format)  Auto Updated every 15min |
| NLD Police | https://thanksforallthefish.nl/log4j_urls.txt (line-by-line)  Auto Updated every 15min |
| NLD Police | https://thanksforallthefish.nl/log4j_blocklist.txt (line-by-line)  Not Verified |


## List of IoC's from security vendors

| Note     | Date of Report | Link |
|:----------------|:----------------|:----------------|
| Talos Intelligence | Almost Daily | https://blog.talosintelligence.com/2021/12/apache-log4j-rce-vulnerability.html |
| 360 Netlab  | 11-12-2021 | https://blog.netlab.360.com/threat-alert-log4j-vulnerability-has-been-adopted-by-two-linux-botnets/ |
| 360 Netlab (Additional) | 13-12-2021 | https://blog.netlab.360.com/ten-families-of-malicious-samples-are-spreading-using-the-log4j2-vulnerability-now/ |
| Microsoft(Contains scan IP's) | Almost Daily | https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Sample%20Data/Feeds/Log4j_IOC_List.csv |
| RedDrip7 | 15-12-2021 | https://github.com/RedDrip7/Log4Shell_CVE-2021-44228_related_attacks_IOCs |
| Cado | 13-12-2021 | https://www.cadosecurity.com/analysis-of-initial-in-the-wild-attacks-exploiting-log4shell-log4j-cve-2021-44228/ |
| CrowdSec (Scan IP validation)| Dynamically updated | https://gist.github.com/blotus/f87ed46718bfdc634c9081110d243166 |
| CrowdStrike | 29-12-2021 | https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/ |
| Cyble | 13-12-2021 | https://blog.cyble.com/2021/12/13/log4j-rce-0-day-vulnerability-in-java-actively-exploited/ |
| CyStack | 28-12-2021 | https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability |
| Fortinet | 21-12-2021 | https://www.fortinet.com/blog/threat-research/critical-apache-log4j-log4shell-vulnerability-what-you-need-to-know |
| NCC Group (Contains scan IP's) | 12-12-2021 | https://research.nccgroup.com/2021/12/12/log4shell-reconnaissance-and-post-exploitation-network-detection/ |
| Lacework | 12-12-2021 | https://www.lacework.com/blog/lacework-labs-identifies-log4j-attackers/ |
| Securelist by Kaspersky | 13-12-2021 | https://securelist.com/cve-2021-44228-vulnerability-in-apache-log4j-library/ |
| RiskIQ (IP's contain scan IP's) | 13-12-2021 | https://community.riskiq.com/article/57abbfcf/indicators |
| Valtix | 14-12-2021 | https://valtix.com/blog/log4shell-observations/ |
| Infoblox | 13-12-2021 | https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/log4j-exploit-harvesting/ |
| Orange Cyberdefense (IP's contain scan IP's) | Almost Daily | https://github.com/Orange-Cyberdefense/log4shell_iocs |

## List of IoC's from Honeypot's
| Note   | Date of Report | Threat  | Links |
|:----------------|:----------------|:----------------|:----------------|
| GelosSnake | 10-12-2021| Kinsing | https://twitter.com/GelosSnake/status/1469341429541576715 |
| CronUp  | 13-12-2021 | Kinsing, Mirai, Muhstik | https://github.com/CronUp/Malware-IOCs/blob/main/2021-12-11_Log4Shell_Botnets |
| CronUp (2) | 19-12-2021 | Kinsing, Mirai | https://github.com/CronUp/Malware-IOCs/blob/main/2021-12-19_MiraiLog4ShellWorm |
| yt0ng | 15-12-2021 | Muhstik, Monero Miner | https://gist.github.com/yt0ng/8a87f4328c8c6cde327406ef11e68726 |
| Maik Morgenstern | 16-12-2021| Backdoor.Ganiw.A | https://twitter.com/TriggerMeHappy/status/1471488408916615169 |
| eromang | 21-12-2021 | Backdoor.Ganiw.A, Mirai, Monero Miner | https://github.com/eromang/researches/tree/main/CVE-2021-44228 |
| NOC.org | Dynamicly updated | Various | https://reputation.noc.org/jndi-attack-logs/ |


## Twitter IoC search tool
| Note     | Links |
|:----------------|:----------------|
| TweetFeed  | https://twitter.com/0xdaniellopez/status/1470029308152487940?s=21 |
