# Log4j overview IoCs

This page contains an overview of any Indicators of Compromise regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known IOCs which can be used to detect and block. Furthermore any references will contain specific information regarding indicator reports.

**NCSC-NL has not verified the IoCs listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide IoCs from reliable sources.**

## Network related IoC's
| Note     | Links |
|:----------------|:----------------|
| The list of callback servers, updated by Greynoise  | [source](https://gist.github.com/superducktoes/9b742f7b44c71b4a0d19790228ce85d8) |
| The list of scanning IP's, updated by Greynoise  | [source](https://gist.github.com/gnremy/c546c7911d5f876f263309d7161a7217) |
| Threatfox  | [source](https://threatfox.abuse.ch/browse/tag/log4j/) |
| UrlHaus  | [source](https://urlhaus.abuse.ch/browse/tag/log4j/) |
| Malware Bazaar | [source](https://bazaar.abuse.ch/browse/tag/log4j/) |
| CTCI | [source](https://docs.google.com/spreadsheets/d/e/2PACX-1vT1hFu_VlZazvc_xsNvXK2GJbPBCDvhgjfCTbNHJoP6ySFu05sIN09neV73tr-oYm8lo42qI_Y0whNB/pubhtml#) |
| Malwar3Ninja | [source](https://twitter.com/bad_packets/status/1469225135504650240)|


## List of IoC's from security vendors

| Note     | Links |
|:----------------|:----------------|
| Talos Intelligence  | [source](https://blog.talosintelligence.com/2021/12/apache-log4j-rce-vulnerability.html)|
| 360 Netlab  | [source](https://blog.netlab.360.com/threat-alert-log4j-vulnerability-has-been-adopted-by-two-linux-botnet)|
| Microsoft(Contains scan IP's) | [source](https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Sample%20Data/Feeds/Log4j_IOC_List.csv)|
| RedDrip7 | [source](https://github.com/RedDrip7/Log4Shell_CVE-2021-44228_related_attacks_IOCs)|
| CrowdSec (Scan IP validation)| [source](https://gist.github.com/blotus/f87ed46718bfdc634c9081110d243166)|
| Bad Packets (Contains scan IP's)| [source](https://gist.github.com/blotus/f87ed46718bfdc634c9081110d243166)|
| NCC Group (Contains scan IP's) | [source](https://research.nccgroup.com/2021/12/12/log4shell-reconnaissance-and-post-exploitation-network-detection/)|
| Lacework | [source](https://www.lacework.com/blog/lacework-labs-identifies-log4j-attackers/)|

## List of IoC's from Honeypot's
| Note     | Links |
|:----------------|:----------------|
| GelosSnake  | [source](https://twitter.com/GelosSnake/status/1469341429541576715)|
| CronUp  | [source](https://github.com/CronUp/Malware-IOCs/blob/main/2021-12-11_Log4Shell_Botnets)|
| yt0ng  | [source](https://gist.github.com/yt0ng/8a87f4328c8c6cde327406ef11e68726)|
| eromang | [source](https://github.com/eromang/researches/tree/main/CVE-2021-44228)|


## Twitter IoC search tool
| Note     | Links |
|:----------------|:----------------|
| TweetFeed  | [source](https://twitter.com/0xdaniellopez/status/1470029308152487940?s=21)|
