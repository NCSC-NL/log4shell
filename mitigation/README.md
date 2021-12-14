# Log4j overview Detection rules and software

This page contains an overview of any detection software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known rules to detect Log4j presence or (suspected) Exploitation. Futhermore any references will contain specific information regarding detection.

**NCSC-NL has not verified the rules and detection software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide rules and detection software from reliable sources.**

## Detection Regex

### Overall detection regex

```plain
\${(\${(.*?:|.*?:.*?:-)('|"|`)*(?1)}*|[jndi:lapsrm]('|"|`)*}*){9,11}
```

#### Caveats
- Please note that due to nested resolution of `${...}` and multiple available obfuscation methods, this regular expression may not detect all forms of exploitation. It is impossible to write exhaustive regular expression.
- This regular expression only works on URL-decoded logs. URL encoding is a popular second layer of obfuscation currently in use by attackers.
- This regular expression searches for the original strings supplied by the attacker. These only remain in their original, unresolved form in the logs of non-vulnerable applications, such as WAF or reverse proxy with ability to log before the vulnerable code is executed. **They are not present in the logs of a vulnerable application.**

#### Logs in vulnerable applications

This detection regex would not have matches in a log of vulnerable application, because only the result of `${...}` resolution is stored instead of the original pattern. Presence of any of these signatures is a strong sign of successful exploitation in these applications:

```plain
com.sun.jndi.
com.sun.jndi.dns.DnsContext
com.sun.jndi.ldap.LdapCtx
Error looking up JNDI resource
```

## Closed source intelligence

| Supplier        | Product         | Links / Rule|
|:----------------|:----------------|:---------------:|
| Akamai       | Cloud | https://www.akamai.com/blog/news/CVE-2021-44228-Zero-Day-Vulnerability |
| Cloudflare   | Cloud | https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/ |
| Citrix     | Citrix WAF | https://www.citrix.com/blogs/2021/12/13/guidance-for-reducing-apache-log4j-security-vulnerability-risk-with-citrix-waf/ |
| Elastic      | Elastic | https://www.elastic.co/blog/detecting-log4j2-with-elastic-security |
| Fortinet      | FortiEDR | https://community.fortinet.com/t5/FortiEDR/Technical-Tip-How-FortiEDR-protects-against-the-exploitation-of/ta-p/201027 |
| Google       | Cloud | https://cloud.google.com/blog/products/identity-security/cloud-armor-waf-rule-to-help-address-apache-log4j-vulnerability |
| Gravwell     | Gravwell | https://www.gravwell.io/blog/cve-2021-44228-log4j-does-not-impact-gravwell-products |
| Microsoft    | Defender | https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/ |
| Microsoft    | Sentinel| https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/ |
| Palo Alto Networks   | Prisma Cloud | https://unit42.paloaltonetworks.com/apache-log4j-vulnerability-cve-2021-44228/ |
| Palo Alto Networks   | Firewall | Threat ID 91991 ingested after content update 8498 |
| Tanium   | Tanium | https://community.tanium.com/s/article/How-Tanium-Can-Help-with-CVE-2021-44228-Log4Shell |
| Tenable  | Nessus | https://www.tenable.com/plugins/search?q=cves%3A%28%22CVE-2021-44228%22%29&sort=&page=1 |
| Tenable  | Nessus, Cloud and on prem | https://community.tenable.com/s/article/Plugins-associated-with-CVE-2021-44228-Log4Shell  |
| Trend Micro | Cloud One| LI Rule 1011241 (See also https://success.trendmicro.com/solution/000289946) |
| Qualys  | Cloud Platform | https://blog.qualys.com/vulnerabilities-threat-research/2021/12/10/apache-log4j2-zero-day-exploited-in-the-wild-log4shell |
| RSA  | NetWitness | client.all contains "${j" || client.all contains "${J" for possible exploitation use direction = 'outbound' && filetype = 'java class' |
| Rapid7   | InsightVM and Nexpose | https://www.rapid7.com/blog/post/2021/12/10/widespread-exploitation-of-critical-remote-code-execution-in-apache-log4j/ |
| Splunk | Splunk | https://www.splunk.com/en_us/blog/security/log-jammin-log4j-2-rce.html |
| Splunk | Splunk | https://www.splunk.com/en_us/blog/security/log4shell-detecting-log4j-vulnerability-cve-2021-44228-continued.html |
| Siemplify  | SOAR platform | https://blog.reconinfosec.com/recons-soar-playbook-to-detect-the-log4j-exploit/ |
| Vectra  | Cognito Detect and Cognito Recall | https://www.vectra.ai/blogpost/cve-2021-44228-log4j-zero-day-affecting-the-internet |

## Opensource Intelligence


### Network based detection
| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
|  NCC Group / Fox-IT | Log4Shell: Reconnaissance and post exploitation network detection | [source](https://research.nccgroup.com/2021/12/12/log4shell-reconnaissance-and-post-exploitation-network-detection/) |

Snort and Suricata rules:

| Note             | Rule-range        | Rule |
|:----------------|:----------------|:---------------:|
| These are ET Open free community detections to alert on current exploit activity.  | SID range 2034647-2034652. | [source](https://rules.emergingthreatspro.com/open/) |

### Web-server mitigation
| Web-server      | Source          | Notes           | Links |
|:----------------|:----------------|:----------------|:---------------:|
| Nginx           | Infiniroot      | Block requests with known patterns in URI and headers using LUA | [Github](https://github.com/infiniroot/nginx-mitigate-log4shell) |


### Host based detection

| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| Neo23x0   | Florian Roth Grep and YARA rule for log4j2 exploitation | https://gist.github.com/Neo23x0/e4c8b03ff8cdf1fa63b7d15db6e3860b |
| Neo23x0   | Florian Roth Detects exploitation attempt against log4j RCE vulnerability fields (Sigma rule) | https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j_fields.yml |
| Neo23x0   | Florian Roth Detects exploitation attempt against log4j RCE vulnerability (Sigma rule) | https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j.yml |
| Neo23x0   | Florian Roth Fenrir Simple IOC scanner bash script | https://github.com/Neo23x0/Fenrir |
