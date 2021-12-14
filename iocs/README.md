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
| cert-agid.gov.it | https://cert-agid.gov.it/download/log4shell-iocs.txt |

## List of IoC's from security vendors

| Note     | Links |
|:----------------|:----------------|
| Talos Intelligence  | https://blog.talosintelligence.com/2021/12/apache-log4j-rce-vulnerability.html |
| 360 Netlab  | https://blog.netlab.360.com/threat-alert-log4j-vulnerability-has-been-adopted-by-two-linux-botnet |
| 360 Netlab (Additional) | https://blog.netlab.360.com/ten-families-of-malicious-samples-are-spreading-using-the-log4j2-vulnerability-now/ |
| Microsoft(Contains scan IP's) | https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Sample%20Data/Feeds/Log4j_IOC_List.csv |
| RedDrip7 | https://github.com/RedDrip7/Log4Shell_CVE-2021-44228_related_attacks_IOCs |
| CrowdSec (Scan IP validation)| https://gist.github.com/blotus/f87ed46718bfdc634c9081110d243166 |
| Bad Packets (Contains scan IP's)| https://gist.github.com/blotus/f87ed46718bfdc634c9081110d243166 |
| NCC Group (Contains scan IP's) | https://research.nccgroup.com/2021/12/12/log4shell-reconnaissance-and-post-exploitation-network-detection/ |
| Lacework | https://www.lacework.com/blog/lacework-labs-identifies-log4j-attackers/ |
| Securelist by Kaspersky | https://securelist.com/cve-2021-44228-vulnerability-in-apache-log4j-library/ |
| RiskIQ (IP's contain scan IP's) | https://community.riskiq.com/article/57abbfcf/indicators |
| Valtix | https://valtix.com/blog/log4shell-observations/ |
| Infoblox | https://blogs.infoblox.com/cyber-threat-intelligence/cyber-campaign-briefs/log4j-exploit-harvesting/ |

## List of IoC's from Honeypot's
| Note     | Links |
|:----------------|:----------------|
| GelosSnake  | https://twitter.com/GelosSnake/status/1469341429541576715 |
| CronUp  | https://github.com/CronUp/Malware-IOCs/blob/main/2021-12-11_Log4Shell_Botnets |
| yt0ng  | https://gist.github.com/yt0ng/8a87f4328c8c6cde327406ef11e68726 |
| eromang | https://github.com/eromang/researches/tree/main/CVE-2021-44228 |


## Twitter IoC search tool
| Note     | Links |
|:----------------|:----------------|
| TweetFeed  | https://twitter.com/0xdaniellopez/status/1470029308152487940?s=21 |
