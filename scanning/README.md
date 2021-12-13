# Log4j overview IoCs

This page contains an overview of any Scanners regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known scanners which can be used to detect vulnerable systems. Furthermore any references will contain specific information regarding indicator reports.

## Scanning overview
| Name      | Description       | Link      |
|:----------|:------------------|:----------|
| Northwave Log4j checker | Scans specified url with a `GET` with payload in url or *User Agent* | https://github.com/NorthwaveSecurity/log4jcheck|
| log4jcheck | Scans a list of URLs with `GET` or `POST` request in combination with user defined parameters | https://github.com/OlafHaalstra/log4jcheck |
| log4j_rce_check | Scans specified host with payload in the *User Agent* | https://gist.github.com/byt3bl33d3r/46661bc206d323e6770907d259e009b6 |

## Scanning utilities
| Name      | Description | Link        |
|:----------|:------------------|:----------|
| Huntress Log4Shell Vulnerability Tester | Creates a JNDI string which calls back to a uniquely generated URL for which can be checked if there are any inbound connections | https://log4shell.huntress.com/ |
| Canary Tokens | Amongst other a Log4Shell JNDI string with URL can be generated for which the DNS queries are logged and presented in an overview with caller information. | https://canarytokens.org/generate |