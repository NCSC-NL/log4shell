# Log4j Detection rules and software

This page contains an overview of any detection software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known rules to detect Log4j presence or (suspected) exploitation. Furthermore any references will contain specific information regarding detection.

**NCSC-NL has not verified the rules and software listed below and therefore cannot guarantee the validity of said rules.
However NCSC-NL strives to provide rules and detection software from reliable sources.**

## Detection Regex

### Overall JNDI detection regex

```plain
\${(\${(.*?:|.*?:.*?:-)('|"|`)*(?1)}*|[jndi:lapsrm]('|"|`)*}*){9,11}
```

#### Caveats
- Please note that due to nested resolution of `${...}` and multiple available obfuscation methods, this regular expression may not detect all forms of exploitation. It is impossible to write exhaustive regular expression.
- This regular expression only works on URL-decoded logs. URL encoding is a popular second layer of obfuscation currently in use by attackers. 

> **Warning:** In a non-vulnerable Log4J instance injected JNDI strings will be logged but not evaluated. However the presence of injected JNDI strings in log files written to by Log4J does not mean your Log4J instance is not vulnerable, since JNDI strings might also be logged (and evaluated) in vulnerable Log4J instances. See the *Logs in vulnerable applications* section below for more details.

### Logs in vulnerable applications
Injected JNDI strings are displayed differently in log files written to by a vulnerable Log4J instance depending on the situation. A JNDI string is always evaluated first (i.e. a DNS/LDAP/RMI request is sent). Depending on the response a different result is logged:

- In case no response is received, the injected JNDI string will be displayed.
- In case a response is received the corresponding classname will be logged such as `com.sun.jndi.dns.DnsContext@<hashcode>` for DNS. In case of RMI the loaded local class will be displayed, for example `javax.el.ELProcessor@<hashcode>`, but this might be any class on the vulnerable host loaded by an attacker.
- Some cases have been observed where LDAP requests are being sent and a malicious class being loaded/executed, but no logging was written by Log4J, probably due to Log4J crashing while executing/evaluation the provided class. 

> **Java Hashcodes**:
When an object is printed it is followed by a `@<hashcode>`. For example: `com.sun.jndi.dns.DnsContext@28a418fc`. Java uses the hash of an object to perform actions such as sorting a collection of object. For more information see [Object::hashCode](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#hashCode()).

Presence of these signatures in log files written to by Log4J is a strong sign of successful exploitation, but you should investigate whether these signatures appeared due to your own actions (i.e. Log4J scanning tools):

Class signatures:
```plain
com.sun.jndi.dns.DnsContext
com.sun.jndi.ldap.LdapCtx
javax.el.ElProcessor
groovy.lang.GroovyShell
```
**Note:** Hashcodes are omitted because they change based on the value in the fields of Java object.

> **Warning**: Since RMI can be used to load classes on the vulnerable Log4J system the list presented here cannot be seen as a complete. Other classes might be loaded and misused to manipulate the system.**

More generic strings:
```plain
com.sun.jndi.
Error looking up JNDI resource
```

## Closed source intelligence

| Supplier        | Product         | Links / Rule|
|:----------------|:----------------|:---------------:|
| Akamai       | Cloud | https://www.akamai.com/blog/news/CVE-2021-44228-Zero-Day-Vulnerability |
| AWS          | Cloud | https://aws.amazon.com/blogs/security/using-aws-security-services-to-protect-against-detect-and-respond-to-the-log4j-vulnerability/ |
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
| Secure2me | Network Intrusion Detection | https://www.secureme2.eu/log4j2-vulnerability/ |
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

### Generic detection guidance

| Source      | Notes        | Links |
|:----------------|:----------------|:---------------:|
| w4rguy   | Gerrit Kortlever guidance on which detections can take place in different steps of the attack, which conclusions can be derived from them and which logs are required to detect the attempts | https://github.com/NCSC-NL/log4shell/tree/main/mitigation/Log4j%20Attack%20Detection%20Guidance%20-%20Release.pdf |
