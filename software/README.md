# Log4j overview related software

This page contains an overview of any related software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known vulnerable and not vulnerable software. Futhermore any reference to the software will contain specific information regarding which version contains the security fixes, and which software still requires mitigation. Please note that this vulnerability may also occur in custom software developed within your organisation. These occurrences are not registered in this overview.

NCSC-NL will use the following status:

| Status         | Description                  |
|:---------------|:-----------------------------|
| Vulnerable     | Software is vulnerable for CVE-2021-44228. |
| Fix            | Software contains a fix for CVE-2021-44228 |
| Workaround | Software is vulnerable but mitigation steps are available |
| Not vuln     | Software is **NOT** vulnerable for CVE-2021-44228. |
| Investigation     | Software is under investigation whether it is vulnerable or not |

The `Version` relates to the `Status` column. If `Status` is Vulnerable, Version indicates vulnerable version(s). If `Status` is Fix, Version indicates the fixed version(s).

**NCSC-NL has published a HIGH/HIGH advisory for the Log4j vulnerability. Normally we would update the HIGH/HIGH advisory for vulnerable software packages, however due to the extensive amounts of expected updates we have created a list of known vulnerable software in the software directory.**

## Software overview

### A

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Acronis       | All |  | Investigation | See further information below| [source](https://security-advisory.acronis.com/advisories/SEC-3859)
| Acronis       | Cyber Backup | 12.5 | Not vuln | | [source](https://security-advisory.acronis.com/advisories/SEC-3859)
| Acronis       | Cyber Files | 8.6.2 onwards | Not vuln | | [source](https://security-advisory.acronis.com/advisories/SEC-3859)
| Acronis       | Cyber Infrastrcuture | 3.5 and 4.x  | Not vuln | | [source](https://security-advisory.acronis.com/advisories/SEC-3859)
| Acronis       | Cyber Protection Home Office | 2017 onwards | Not vuln | | [source](https://security-advisory.acronis.com/advisories/SEC-3859)
| AIL           | AIL | all | Not vuln | | [source](https://twitter.com/ail_project/status/1470373644279119875)
| Akamai        | Siem Splunk Connector | Unknown to latest | Vulnerable |[source](https://github.com/akamai/siem-splunk-connector) |
| Amazon        | AWS CloudHSM | < 3.4.1. | Fix | |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | AWS Lambda | Unknown | Fix | Vulnerable when using aws-lambda-java-log4j2 |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | EC2 |Amazon Linux 1 & 2 | Vulnerable | Default packages not vulnerable |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | OpenSearch | Unknown | Fix | |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Apache        | Camel | all | Not vuln | |[source](https://camel.apache.org/blog/2021/12/log4j2/) |
| Apache        | Cassandra | all | Not vuln | |[source](https://lists.apache.org/thread/2rngylxw8bjos6xbo1krp29m9wn2hhdr) |
| Apache        | Druid | 0.22.1 | Fix | |[source](https://github.com/apache/druid/pull/12051) |
| Apache        | Flink | 1.15.0, 1.14.1, 1.13.4 | Fix | |[source](https://issues.apache.org/jira/browse/FLINK-25240) |
| Apache        | Kafka | all | Not vuln | Uses log4j 1.x |[source](https://lists.apache.org/thread/lgbtvvmy68p0059yoyn9qxzosdmx4jdv) |
| Apache        | Karaf | Unknown | Vulnerable | Depends on [PAX logging](https://github.com/ops4j/org.ops4j.pax.logging/issues/414) which is affected |[source](https://mail-archives.apache.org/mod_mbox/karaf-dev/202112.mbox/browser) |
| Apache        | Log4j | 2.15.0 | Fix | |[source](https://logging.apache.org/log4j/2.x/security.html) |
| Apache        | SOLR | 7.4.0 to 7.7.3, 8.0.0 to 8.11.0 | Fix | Versions before 7.4 also vulnerable when using several configurations |[source](https://solr.apache.org/security.html#apache-solr-affected-by-apache-log4j-cve-2021-44228) |
| Apache        | Tika | 2.0.0 and up | Vulnerable | |[source](https://tika.apache.org/2.0.0/index.html) |
| Apache        | Tomcat|| Not vuln|| [source](https://tomcat.apache.org/tomcat-9.0-doc/logging.html) |
| Apache        | Zookeeper|| Not vuln| Zookeeper uses Log4j 1.2 version | [source](https://issues.apache.org/jira/browse/ZOOKEEPER-4423) |
| APC           | PowerChute Business Edition | Unknow to 10.0.2.301 | Vulnerable |  |  |
| APC           | PowerChute Network Shutdown | Unknow to 4.2.0 | Vulnerable |  |  |
| Apereo        | CAS | 6.3.x & 6.4.x | Fix | Other versions still in active maintainance might need manual inspection |[source](https://apereo.github.io/2021/12/11/log4j-vuln/) |
| Apereo        | Opencast | < 9.10, < 10.6 | Fix | |[source](https://github.com/opencast/opencast/security/advisories/GHSA-mf4f-j588-5xm8) |
| Apigee        | Edge and OPDK products | All version | Not vuln | |[source](https://status.apigee.com/incidents/3cgzb0q2r10p) |
| Aptible       | Aptible | ElasticSearch 5.x | Fix | | [source](https://status.aptible.com/incidents/gk1rh440h36s?u=zfbcrbt2lkv4) |
| Arduino        | Arduino IDE | 1.8.17 | Fix |[source](https://support.arduino.cc/hc/en-us/articles/4412377144338-Arduino-s-response-to-Log4j2-vulnerability-CVE-2021-44228) |
| Atlassian     | Bamboo Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | BitBucket Server | On prem | Workaround | [source](https://community.atlassian.com/t5/Bamboo-questions/Re-log4j-zero-day/qaq-p/1886739/comment-id/30819#M30819)
| Atlassian     | Confluence Server & Data Center| On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Crowd Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Crucible | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Fisheye | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Jira Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Avaya         | | | | [source](https://support.avaya.com/helpcenter/getGenericDetails?detailId=1399839287609) |
| Azure         | Data lake store java | < 2.3.10 | Not vuln | Fix has been made to upgrade log4j-core. But this dependency has scope 'test' meaning it is not part of the final product/artifact. So there's no risk for end users here. |[source](https://github.com/Azure/azure-data-lake-store-java/blob/ed5d6304783286c3cfff0a1dee457a922e23ad48/CHANGES.md#version-2310) |

### B

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Backblaze      | Cloud | N/A (SaaS) | Fix | Cloud service patched |[source](https://help.backblaze.com/hc/en-us/articles/4412580603419) |
| BeyondTrust    | Privilege Management Cloud | Unknown | Vulnerable | [source](https://beyondtrustcorp.service-now.com/kb_view.do?sysparm_article=KB0016542) |
| BeyondTrust    | Privilege Management Reporting | Unknown | Vulnerable | [source](https://beyondtrustcorp.service-now.com/kb_view.do?sysparm_article=KB0016542) |
| BigBlueButton   | BigBlueButton | Unknown | Not vuln | |[source](https://github.com/bigbluebutton/bigbluebutton/issues/13897) |
| Bitdefender   | GravityZone On-Premises | Unknown | Not vuln | |[source](https://businessinsights.bitdefender.com/security-advisory-bitdefender-response-to-critical-0-day-apache-log4j2-vulnerability) |
| Bitnami       | Unknown | Unknown | Fix | |[source](https://docs.bitnami.com/general/security/security-2021-12-10/) |
| Brian Pangburn | SwingSet | < 4.0.6 | Fix | |[source](https://github.com/bpangburn/swingset/releases/tag/swingset-4.0.6) |
| Broadcom      | CA Advanced Authentication | 9.1 & 9.1.01 & 9.1.02 | Workaround | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection Manager (SEPM) | 14.3 | Workaround | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Advanced Secure Gateway (ASG) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | BCAAA | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Content Analysis (CA)(SEPM) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Protection (CWP) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Protection for Storage (CWP:S) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Critical System Protection (CSP) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Email Security Service (ESS) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | HSM Agent | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Information Centric Analytics (ICA) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Industrial Control System Protection (ICSP) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | IT Analytics (ITA) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | IT Management Suite | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 API Gateway | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 Mobile API Gateway | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Integrated Cyber Defense Manager (ICDm) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Integrated Cyber Defense Exchange (ICDx) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Integrated Secure Gateway (ISG) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 API Developer Portal | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | LiveUpdate Administrator (LUA) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Management Center (MC) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | PacketShaper (PS) S-Series | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | PolicyCenter (PC) S-Series | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | ProxySG | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Security Analytics (SA) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | ServiceDesk | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Directory | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Control Compliance Suite (CCS) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection (SEP) Agent | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Access Manager | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Access Manager Server Control | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Identity Manager | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Reporter | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Secure Access Cloud (SAC) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | SiteMinder (CA Single Sign-On) | 12.8.x Policy Server, 12.8.04 or later Administrative UI, 12.8.x Access Gateway, 12.8.x SDK, 12.7 and 12.8 ASA Agents | Fix, Workaround | |[source](https://knowledge.broadcom.com/external/article?articleId=230270) |
| Broadcom      | SSL Visibility (SSLV)| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Detection and Response (EDR) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Encryption (SEE) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection (SEP)| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection (SEP) for Mobile| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Mail Security for Microsoft Exchange (SMSMSE) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Messaging Gateway (SMG) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Protection Engine (SPE) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Protection for SharePoint Servers (SPSS) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | VIP Authentication Hub | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Web Isolation (WI) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Web Security Service (WSS)) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | WebPulse | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | CloudSOC Cloud Access Security Broker (CASB) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Assurance (CWA) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Protection for Storage (CWP:S) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Control Compliance Suite (CCS) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Data Center Security (DCS) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Data Loss Prevention (DLP) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Ghost Solution Suite (GSS) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | IT Management Suite | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 API Gateway | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 Mobile API Gateway | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | ProxySG | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Security Analytics (SA) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Directory | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Identity Governance and Administration (IGA)| Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec PGP Solutions | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | VIP | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |

### C

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Carbon Black | Cloud Workload Appliance | Unknown | Mitigation | More information on pages linked bottom of blogpost (behind login)| [source](https://community.carbonblack.com/t5/Documentation-Downloads/Log4Shell-Log4j-Remote-Code-Execution-CVE-2021-44228/ta-p/109134) |
| Carbon Black | EDR Servers| Unknown | Mitigation | More information on pages linked bottom of blogpost (behind login)| [source](https://community.carbonblack.com/t5/Documentation-Downloads/Log4Shell-Log4j-Remote-Code-Execution-CVE-2021-44228/ta-p/109134) |
| Cerebro | Cerebro Elasticsearch Web Admin | All | Not vuln | Uses logback for logging |[source](https://github.com/lmenezes/cerebro/blob/main/conf/logback.xml#L5) |
| Cerberus | FTP | Unknown | Not vuln | |[source](https://support.cerberusftp.com/hc/en-us/articles/4412448183571-Cerberus-is-not-affected-by-CVE-2021-44228-log4j-0-day-vulnerability) |
| Cerebrate | Cerebrate | All | Not vuln | |[source](https://twitter.com/cerebrateproje1/status/1470347775141421058) |
| Check Point | Quantum Security Gateway | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point | Quantum Security Management | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point| CloudGuard | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point | Infinity Portal | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point | Harmony Endpoint & Harmony Mobile | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point | SMB | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Check Point | ThreatCloud | All | Not vuln | |[source](https://supportcontent.checkpoint.com/solutions?id=sk176865) |
| Chef | Infra Server | All | Not vuln | | [source](https://www.chef.io/blog/is-chef-vulnerable-to-cve-2021-44228-(log4j))|
| Chef | Automate | All | Not vuln | | [source](https://www.chef.io/blog/is-chef-vulnerable-to-cve-2021-44228-(log4j))|
| Chef | Backend | All | Not vuln | | [source](https://www.chef.io/blog/is-chef-vulnerable-to-cve-2021-44228-(log4j))|
| Cisco | General Cisco Disclaimer | Cisco is updating their advisory three times a day, please keep their website in your watchlist. We will try to update accordingly ||||
| Cisco | AnyConnect Secure Mobility Client | All versions | Not vuln | | [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SocialMiner|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Extensible Network Controller (XNC)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Data Broker|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Insights|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Wide Area Application Services (WAAS)|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco AMP Virtual Private Cloud Appliance|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Adaptive Security Appliance (ASA) Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Advanced Web Security Reporting Application|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Content Security Management Appliance (SMA)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Email Security Appliance (ESA)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower 4100 Series|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower 9300 Security Appliances|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower Management Center|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower Threat Defense (FTD)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Identity Services Engine (ISE)|Unknown|Vulnerable||[source](https://tools.cisco.com/bugsearch/bug/CS
47133)|
|Cisco|Cisco Web Security Appliance (WSA)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ACI Multi-Site Orchestrator|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Application Policy Infrastructure Controller (APIC)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco CloudCenter Suite Admin|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco CloudCenter Workload Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Connected Grid Device Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Connected Mobile Experiences|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Crosswork Change Automation|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco DNA Assurance|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Data Center Network Manager (DCNM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Elastic Services Controller (ESC)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IoT Field Network Director (formerly Cisco Connected Grid Network Management System)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Modeling Labs|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Planner|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Services Orchestrator (NSO)|< nso-5.3.5.1, nso-5.4.5.2, nso-5.5.4.1, nso-5.6.3.1|Vulnerable|Fixes expected 17-Dec|[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Dashboard (formerly Cisco Application Services Engine)|<2.1.2|Vulnerable|Patch expected 7-jan-2022|[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Optical Network Planner|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Policy Suite|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Central for Service Providers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Assurance|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Provisioning|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Infrastructure|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime License Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Network Registrar|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Optical for Service Providers|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Provisioning|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Service Catalog|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco UCS Performance Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Virtual Topology System - Virtual Topology Controller (VTC) VM|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco WAN Automation Engine (WAE)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ACI Virtual Edge|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ASR 5000 Series Routers|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco DNA Center|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Enterprise NFV Infrastructure Software (NFVIS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco GGSN Gateway GPRS Support Node|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IOS and IOS XE Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IOx Fog Director|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IP Services Gateway (IPSG)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco MDS 9000 Series Multilayer Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco MME Mobility Management Entity|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Mobility Unified Reporting and Analytics System|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Assurance Engine|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Convergence System 2000 Series|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 5500 Platform Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 5600 Platform Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 6000 Series Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 7000 Series Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 9000 Series Fabric Switches in Application Centric Infrastructure (ACI) mode|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco PDSN/HA Packet Data Serving Node and Home Agent|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco PGW Packet Data Network Gateway|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 1000 Series Routers|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 2000 Series Routers|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 5000 Series Routers|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge Cloud Router Platform|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vManage|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Secure Network Analytics (SNA), formerly Stealthwatch|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco System Architecture Evolution Gateway (SAEGW)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco HyperFlex System|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco UCS Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco BroadWorks|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Broadcloud Calling|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Computer Telephony Integration Object Server (CTIOS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Contact Center Domain Manager (CCDM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Contact Center Management Portal (CCMP)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Emergency Responder|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Enterprise Chat and Email|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Finesse|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Packaged Contact Center Enterprise|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Paging Server (InformaCast)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Paging Server|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Attendant Console Advanced|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Attendant Console Business Edition|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Attendant Console Department Edition|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Attendant Console Enterprise Edition|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Attendant Console Premium Edition|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Contact Center Enterprise|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Contact Center Express|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Customer Voice Portal|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Intelligent Contact Management Enterprise|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified SIP Proxy Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Virtualized Voice Browser|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Exony Virtualized Interaction Manager (VIM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Expressway Series|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Meeting Server|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco TelePresence Management Suite|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco TelePresence Video Communication Server (VCS)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Vision Dynamic Signage Director|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Mobility Services Engine|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco CX Cloud Agent Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Cloud Email Security|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Cognitive Intelligence|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Common Services Platform Collector|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Connectivity|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco DNA Spaces|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Defense Orchestrator|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Intersight|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IoT Operations Dashboard|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Kinetic for Cities|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Assessment (CNA) Tool|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Umbrella|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Managed Services Accelerator (MSX) Network Access Control Service|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|AppDynamics |<21.12.0|Fix||[source](https://docs.appdynamics.com/display/PAA/Security+Advisory%3A+Apache+Log4j+Vulnerability) |
|Cisco|Cisco Webex Meetings Server| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Evolved Programmable Network Manager| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Integrated Management Controller (IMC) Supervisor| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Intersight Virtual Appliance| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco UCS Director| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Contact Center Enterprise - Live Data server| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Video Surveillance Operations Manager| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Communications Manager Cloud| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Webex Cloud-Connected UC (CCUC)| Unknown | Vulnerable || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Duo| Unknown | Fix || [source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Jabber Guest|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Cloud Services Platform 2100|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Cloud Services Platform 5000 Series|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Tetration Analytics|All versions|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Adaptive Security Device Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Registered Envelope Service|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Business Process Automation|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco CloudCenter Action Orchestrator|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Container Platform|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime Access Registrar|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime Cable Provisioning|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime Collaboration Deployment|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime IP Express|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime Network Registrar|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Prime Performance Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Security Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco UCS Central Software|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco IOS XR Software|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Nexus 3000 Series Switches|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Nexus 9000 Series Switches in standalone NX-OS mode|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco UCS C-Series Rack Servers - Integrated Management Controller|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Hosted Collaboration Mediation Fulfillment|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Communications Domain Manager|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Communications Manager / Cisco Unified Communications Manager Session Management Edition|Unknown|Vulnerable||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Communications Manager IM & Presence Service (formerly CUPS)|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unified Intelligence Center|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unity Connection|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Unity Express|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Ultra Packet Core|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|Cisco|Cisco Smart Software Manager On-Prem|Unknown|Not vuln||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) |
|CIS-CAT|CSAT Pro| < 1.7.1 |Vulnerable|Upgrade to v1.7.1 to be released 16/12|[source](https://cisecurity.atlassian.net/servicedesk/customer/portal/15/article/2434301961) |
|CIS-CAT|CIS-CAT Pro Assessor v4| < 4.13.0 |Vulnerable|Upgrade to v4.13.0 to be released 16/12|[source](https://cisecurity.atlassian.net/servicedesk/customer/portal/15/article/2434301961) |
|CIS-CAT|CIS-CAT Pro Assessor Service v4| < 1.13.0 |Vulnerable|Upgrade to v1.13.0 to be released 16/12|[source](https://cisecurity.atlassian.net/servicedesk/customer/portal/15/article/2434301961) |
|CIS-CAT|CIS-CAT Pro Assessor v3| < 3.0.77 |Vulnerable| Upgrade to v3.0.77 to be released 16/12|[source](https://cisecurity.atlassian.net/servicedesk/customer/portal/15/article/2434301961) |
|CIS-CAT|CIS-CAT Pro Dashboard| All| Not vuln||[source](https://cisecurity.atlassian.net/servicedesk/customer/portal/15/article/2434301961) |
| Citrix       | NetScaler ADC | Unknown | Not vuln |  Implementation not using WlonNS feature, is not impacted | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | NetScaler Gateway | Unknown | Not vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Analytics | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Application Delivery Management (NetScaler MAS)  | Unknown | Not vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Hypervisor (XenServer)   | Unknown | Not Vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | SD-WAN  | Unknown | Not vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Virtual Apps and Desktops (XenApp & XenDesktop)    | Unknown | Not vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Workspace  | Unknown | Not vuln  |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Workspace App  | Unknown | Not vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Sharefile  | Unknown | Not vuln  |  | [source](https://support.citrix.com/article/CTX335705) |
| cPanel | cPanel | Unknown | Mitigation | | [source](https://forums.cpanel.net/threads/log4j-cve-2021-44228-does-it-affect-cpanel.696249/) |
| Commvault | All products | All versions | Not vulnerable || [source](https://community.commvault.com/technical-q-a-2/log4j-been-used-in-commvault-1985?postid=11745#post11745) |
| Commvault | Cloud Apps & Oracle & MS-SQL | All supported versions | vulnerable || [source](https://documentation.commvault.com/11.24/essential/146231_security_vulnerability_and_reporting.html) |
| Connect2id | Connect2id server | < 12.5.1 | Fix || [source](https://connect2id.com/blog/connect2id-server-12-5-1) |
| Connectwise | Perch | Unknown | Fix || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Manage on-premise's Global Search  | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Marketplace | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Global search capability of Manage Cloud | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | StratoZen | Unknown | Mitigation | Urgent action for self-hosted versions |[source](https://www.connectwise.com/company/trust/advisories) |
| Contrast | Hosted SaaS Enviroments | All | Fix | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | On-premises (EOP) Environments | All | Fix/Mitigation | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | Java Agent | All | Not vuln | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | Scan | All | Fix | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| ControlUp | All products | All versions | Fix | |[source](https://status.controlup.com/incidents/qqyvh7b1dz8k) |
| Copadata | Zenon product family | All | Not vuln | |[source](https://www.copadata.com/en/support-services/knowledge-base-faq/pare-products-in-the-zenon-product-family-affect-4921/) |
| Coralogix | Coralogix | Unknown | Fix | |[source](https://status.coralogix.com/incidents/zzfn8t0fzdy2?u=1q9952ycm1gr) |
| Couchbase | Couchbase ElasticSearch connector| < 4.3.3 & 4.2.13 | Fix | |[source](https://forums.couchbase.com/t/ann-elasticsearch-connector-4-3-3-4-2-13-fixes-log4j-vulnerability/32402) |
| Cryptshare | Cryptshare Server | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare for Outlook | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare for Notes | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare for NTA 7516 | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare .NET API | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare Java API | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cryptshare | Cryptshare Robot | All | Not vuln | |[source](https://www.cryptshare.com/nl/support/cryptshare-support/) |
| Cyberark  | Cloud Entitlements Manager || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Endpoint Privilege Manager (EPM) - Agents || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Endpoint Privilege Manager (EPM) - EPM Server (On-Premise) || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Endpoint Privilege Manager (EPM) - Service (SaaS) || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | HTML5 Gateway || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Identity - Mobile App || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Identity - On-Premise Components || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Identity - Secure Web Sessions (SWS) || Fix | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Identity - Service (SaaS) || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Legacy Sensitive Information Management (SIM) || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Marketplace components - CPM Plugins || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Marketplace components - Certified and Trusted Marketplace Components || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Marketplace components - PSM Connection Components || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | On-Demand Privileges Manager (OPM) || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | PAS Self Hosted (Vault, PVWA, CPM, PSM, PSMP) || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Privilege Cloud - On-Premise Components || Not Vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Privilege Cloud - Service (SaaS) || Fix | Mitigation applied. No further action required by customers | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Privileged Threat Analytics (PTA) || Workaround | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228), [workaround](https://cyberark-customers.force.com/s/article/PTA-CVE-2021-44228-Mitigation-for-Privilege-Threat-Analytics) |
| Cyberark  | Remote Access (Alero) - Connector || Fix | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Remote Access (Alero) - Mobile App || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Remote Access (Alero) - Service (SaaS) || Fix | Mitigation applied. No further action required by customers | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Secrets Manager Credential Providers || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cyberark  | Secrets Manager Conjur Enterprise || Not vuln | | [source](https://cyberark-customers.force.com/s/article/Critical-Vulnerability-CVE-2021-44228) |
| Cybereason | All Cybereason products | Unknown | Not vuln | |[source](https://www.cybereason.com/blog/cybereason-solutions-are-not-impacted-by-apache-log4j-vulnerability-cve-2021-44228) |

### D

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| DatadogHQ | Datadog Agent | 6 < [6.32.2](https://github.com/DataDog/datadog-agent/releases/tag/6.32.2), 7 < [7.32.2](https://github.com/DataDog/datadog-agent/releases/tag/7.32.2) | Fix/workaround | JMX monitoring component leverages an impacted version of log4j | [source](vendor-statements/DatadogHQ%20-%20Our_response_to_log4j_vulnerability.pdf) |
| DataNet Quality Systems | WinSPC | | Not vuln | Note: this is not **WinSCP**. This is a Statistical Process Control software. | Email from customer support. See vendor-statements folder. |
| Datto | All Datto products | Unknown | Not vuln | |[source](https://www.datto.com/blog/dattos-response-to-log4shell) |
| Datev | All Datev products | Unknown | Vulnerable | german source |[source](https://www.datev-community.de/t5/Freie-Themen/Log4-J-Schwachstelle/td-p/258147) |
| Debian | Apache-log4j.1.2 | stretch, buster, bullseye | Fix | |[source](https://security-tracker.debian.org/tracker/CVE-2021-44228) |
| Debian | Apache-log4j2 | stretch, buster,  bullseye | Fix| |[source](https://security-tracker.debian.org/tracker/CVE-2021-44228) |
| Dell | BSAFE Crypto-C Micro Edition | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | BSAFE Crypto-J | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | BSAFE Micro Edition Suite | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Centera | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Chassis Management Controller (CMC) | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Cloudlink | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Cloud Mobility for Dell EMC Storage | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Data Domain OS | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Disk Library for Mainframe | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Embedded NAS | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Cloud Disaster Recovery | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC DataIQ | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC ECS | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Integrated System for Microsoft Azure Stack Hub | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC License Manager | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC NetWorker | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Networking Onie | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC ObjectScale | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerFlex Appliance | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerFlex Manager | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerFlex Rack | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerMax | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerPath Management Appliance | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerPath | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerProtect Cyber Recovery | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerProtect Data Manager | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerProtect DP Series Appliance (iDPA) | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerScale OneFS | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerShell for PowerMax | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerShell for Powerstore | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerShell for Unity | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerStore | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC PowerSwitch Z9264F-ON BMC, Dell EMC PowerSwitch Z9432F-ON BMC | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC RecoverPoint | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Repository Manager (DRM) | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC SourceOne | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC SRM vApp | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Streaming Data Platform | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Systems Update (DSU) | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Unity | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC Virtual Storage Integrator | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC VPLEX | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC VxRail | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | EMC XtremIO | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Enterprise Hybrid Cloud | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | GeoDrive | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Hybrid Client (DHC) | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | ImageAssist | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Insight IQ | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Integrated Dell Remote Access Controller (iDRAC) | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | IsilonSD Management Server | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Mainframe Enablers | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | MyDell Mobile | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | NetWorker Management Console | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | NetWorker MM for Hyper-V | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking N-Series | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking OS9 | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking OS | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking SD-WAN Edge | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking W-Series | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Networking X-Series | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OMIMSSC (OpenManage Integration for Microsoft System Center) | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OpenManage Change Management | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OpenManage Enterprise | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OpenManage Integration for Microsoft System Center for System Center Operations Manager | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OpenManage Integration with Microsoft Windows Admin Center | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Open Management Enterprise - Modular | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Open Manage Mobile | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | OpenManage Network Integration | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Open Manage Server Administrator | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | PowerEdge BIOS | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Remotely Anywhere | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Secure Connect Gateway (SCG) 5.0 Appliance | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Smart Fabric Storage Software | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Solutions Enabler | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Sonic | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | SRS Policy Manager | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | SRS VE | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | SupportAssist Client Commercial | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | SupportAssist Client Consumer | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | SupportAssist Enterprise | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Unisphere Central | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Unisphere for PowerMax | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Vblock | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | ViPR Controller | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | VNX2 | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | VNX Control Station | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Vsan Ready Nodes | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | VxBlock | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | VxFlex Ready Nodes | Unknown | Investigation |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Wyse Management Suite Import Tool | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Wyse Management Suite | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Wyse Proprietary OS (ThinOS) | Unknown | Not vuln |  | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Dell | Wyse Windows Embedded | Unknown | Vulnerable | Fix Release Timeline TBD | [source](https://www.dell.com/support/kbdoc/nl-nl/000194414/dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Docker | Docker infrastructure | Unknown | Not vuln | Docker infrastructure not vulnerable, Docker images could be vulnerable. For more info see source. |[source](https://www.docker.com/blog/apache-log4j-2-cve-2021-44228/) |
| Dropwizard | Dropwizard | Unknown | Not vuln | Only vulnerable if you manually added Log4j |[source](https://twitter.com/dropwizardio/status/1469285337524580359) |
| Dynatrace | Dynatrace Cloud Services | Unknown | Fix | | [source](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/Impact-of-log4j-zero-day-vulnerability/m-p/177259/highlight/true#M19282) |
| Dynatrace | ActiveGates | 1.229.49.20211210-165018, 1.227.31.20211210-164955, 1.225.29.20211210-164930, 1.223.30.20211210-164926 | Fix | |[source](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/Impact-of-log4j-zero-day-vulnerability/m-p/177259/highlight/true#M19282) |

### E

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| EAL | ATS Classic | All Versions | Not Vuln | | See vendor-statements |
| Elastic         | APM Java Agent | 1.17.0-1.28.0 | Workaround |  Only vulnerable with specific configuration | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | APM Server | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Beats | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Cmd | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Agent | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Cloud | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Cloud Enterprise | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Cloud on Kubernetes | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Endgame | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elastic Maps Service | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Elasticsearch | < 6.8.21, < 7.16.1  | Workaround | Information leakage vulnerability | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Endpoint Security | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Enterprise Search | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Fleet Server | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Kibana | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Logstash | < 6.8.21, < 7.16.1 | Workaround |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Machine Learning | | Not Vuln |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| Elastic         | Swiftype | | Investigation |   | [source](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476) |
| ELO             | Digital Office || Not Vuln || [source](http://www.elo.com)|
| ESET            | All products | Unknown | Not vuln | |[source](https://support.eset.com/en/alert8188-information-regarding-the-log4j2-vulnerability) |
| Esri | ArcGIS Enterprise and related products | < 10.8.0 | Vulnerable |  | [source](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/arcgis-software-and-cve-2021-44228-aka-log4shell-aka-logjam/) |
| EVL Labs | JGAAP | <8.0.2 | Fix | | [source](https://github.com/evllabs/JGAAP/releases/tag/v8.0.2) |
| eXtreme Hosting | All products | Unknown | Not vuln | |[source](https://extremehosting.nl/log4shell-log4j/) |

### F

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
|F5| All products | |Not Vuln | F5 products themselves are not vulnerable, but F5 published guidance on mitigating through BIG-IP ASM/Advanced WAF and NGINX App Protect|[source](https://support.f5.com/csp/article/K19026212)|
|FileCap| All products | <5.1.0 | Vulnerable | Fix: 5.1.1 |[source](https://mailchi.mp/3f82266e0717/filecap-update-version-511)|
| Fiix | CMMS core | V5  | Fix | | [source](https://rockwellautomation.custhelp.com/app/answers/answer_view/a_id/1133605) |
|Forcepoint |DLP Manager                                                                          ||Workaround |[source](https://support.forcepoint.com)|
|Forcepoint |Forcepoint Cloud Security Gateway (CSG)                                              ||Not vuln   |[source](https://support.forcepoint.com)|
|Forcepoint |Next Generation Firewall (NGFW)                                                      ||Not vuln   |[source](https://support.forcepoint.com)|
|Forcepoint |Next Generation Firewall, NGFW VPN Client, Forcepoint User ID service and Sidewinder ||Not vuln   |[source](https://support.forcepoint.com)|
|Forcepoint |One Endpoint                                                                         ||Not vuln   |[source](https://support.forcepoint.com)|
|Forcepoint |Security Manager (Web, Email and DLP)                                                ||Workaround |[source](https://support.forcepoint.com)|
|Forescout | | | Investigation | | [soruce](https://www.forescout.com/blog/forescout%e2%80%99s-response-to-cve-2021-44228-apache-log4j-2/)
|ForgeRock        | Autonomous Identity |  | Workaround | all other ForgeRock products not vuln | [source](https://backstage.forgerock.com/knowledge/kb/book/b21824339#1_bzBa) |
|Fortinet| FortiAIOps| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiAnalyzer Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiAnalyzer| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiAP| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiAuthenticator| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiCASB| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiConvertor| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiDeceptor| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiEDR Agent| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiEDR Cloud| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiGate Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiGSLB Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiMail| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiManager Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiManager| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiNAC| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiNAC| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiOS (includes FortiGate & FortiWiFi)| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiPhish Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiPolicy| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiPortal | |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiRecorder| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiSIEM| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiSOAR| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiSwitch Cloud in FortiLANCloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiSwitch & FortiSwitchManager| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiToken Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiVoice| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| FortiWeb Cloud| |Not Vuln||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|Fortinet| ShieldX| |Vulnerable||[source](https://www.fortiguard.com/psirt/FG-IR-21-245)|
|F-Secure| Endpoint Proxy | 13-15| Fix| |[source](https://status.f-secure.com/incidents/sk8vmr0h34pd)|
|F-Secure| Policy Manager | 13-15| Fix| |[source](https://status.f-secure.com/incidents/sk8vmr0h34pd)|
|F-Secure| Policy Manager Proxy| 13-15| Fix| |[source](https://status.f-secure.com/incidents/sk8vmr0h34pd)|
|FusionAuth| FusionAuth| 1.32|Not Vuln||[source](https://fusionauth.io/blog/2021/12/10/log4j-fusionauth/)|

### G

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Genesys | All products || Investigation ||[source](https://www.genesys.com/blog/post/genesys-update-on-the-apache-log4j-vulnerability)|
| GFI Software | Kerio Connect | | Vulnerable | | [source](https://forums.gfi.com/index.php?t=msg&th=39096&start=0&)|
| GoAnywhere| MFT| Unknown| Workaround | | [source](https://www.goanywhere.com/cve-2021-44228-goanywhere-mitigation-steps)|
| GoAnywhere| Gateway| Unknown| Workaround | | [source](https://www.goanywhere.com/cve-2021-44228-goanywhere-mitigation-steps)|
| GoAnywhere| Agents| Unknown| Workaround | | [source](https://www.goanywhere.com/cve-2021-44228-goanywhere-mitigation-steps)|
| Graylog | Graylog | < 3.3.15,<4.0.14,<4.1.9,<4.2.3 | Fix | | [source](https://www.graylog.org/post/graylog-update-for-log4j)|
| GuardedBox | GuardedBox | <3.1.2 | Fix | | [source](https://twitter.com/GuardedBox/status/1469739834117799939) |

### H

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| HackerOne | Unknown | Unknown | Fix ||[source](https://twitter.com/jobertabma/status/1469490881854013444)|
| Hashicorp| All products | |Not Vuln | | [source](https://support.hashicorp.com/hc/en-us/articles/4412469195795-CVE-2021-44228-Log4J-has-no-impact-on-HashiCorp-Products)|
| HCL Software | BigFix Compliance | Unknown | Workaround | | [source](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0095486)|
| HCL Software | BigFix Inventory | Unknown | Workaround | | [source](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0095486)|
| HCL Software | BigFix Compliance | Unknown | Investigation | | [source](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0095486)|
| HCL Software | BigFix Compliance | Unknown | Investigation | | [source](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0095486)|
| Hexagon | M.App Enterprise | Unknown | Investigation | Might be vulnerable only when used with Geoprocessing Server | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | ERDAS APOLLO Advantage & Professional | Unknown | Investigation | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | GeoMedia | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | IMAGINE | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | ImageStation | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | GeoMedia WebMap | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | Geospatial Portal | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | Geospatial SDI | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | GeoMedia SmartClient | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | ERDAS APOLLO Essentials | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | M.App Enterprise standalone or with Luciad Fusion | Unknown | Not vuln | | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | Luciad Fusion | Unknown | Not vuln | The only risk is if Log4J was implemented outside of the default product install | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hexagon | Luciad Lightspeed | Unknown | Not vuln | The only risk is if Log4J was implemented outside of the default product install | [source](https://supportsi.hexagon.com/help/s/article/Security-Vulnerability-CVE-2021-44228-log4j-2)|
| Hitachi Vantara | Pentaho | v8.3.x, v9.2.x | Not vuln | | [source](https://support.pentaho.com/hc/en-us/articles/4416229254541-log4j-2-zero-day-vulnerability-No-impact-to-supported-versions-of-Pentaho-)|
| HostiFi | Unifi hosting | Unknown | Fix | Hosted Unifi solution | [source](https://twitter.com/hostifi_net/status/1440311322592231436) |
| Huawei | All products | | Investigation | | [source](https://www.huawei.com/en/psirt/security-notices/huawei-sn-20211210-01-log4j2-en)|

### I

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| IBM | All products | | Investigation | | [source](https://www.ibm.com/blogs/psirt/an-update-on-the-apache-log4j-cve-2021-44228-vulnerability/)|
| IBM | Curam SPM | 8.0.0, 7.0.11 | Vulnerable | | [source](https://www.ibm.com/blogs/psirt/security-bulletin-vulnerability-in-apache-log4j-may-affect-cram-social-program-management-cve-2019-17571/)|
| IBM | Sterling Order Management | Unknown | Not vuln | | [source](https://www.ibm.com/support/pages/node/6525544)|
| IBM | Sterling Fulfillment Optimizer | Unknown | Vulnerable | | [source](https://www.ibm.com/support/pages/node/6525544)|
| IBM | Sterling Inventory Visibility | Unknown | Vulnerable | | [source](https://www.ibm.com/support/pages/node/6525544)|
| IBM | VM Manager Tool (part of License Metric Tool) | >9.2.21,<9.2.26 | Vulnerable | | [source](https://www.ibm.com/support/pages/node/6525762/)|
| IBM | Websphere | 8.5 | Vulnerable | fix: PH42728 | [source](https://www.ibm.com/support/pages/node/6525706/)|
| IBM | Websphere | 9.0 | Vulnerable | fix: PH42728 | [source](https://www.ibm.com/support/pages/node/6525706/)|
| IGEL | Universal Management Suite | | Vulnerable | | [source](www.igel.com/support) |
| Inductive Automation | Ignition | All versions | Not Vuln| | [source](https://support.inductiveautomation.com/hc/en-us/articles/4416204541709-Regarding-CVE-2021-44228-Log4j-RCE-0-day) |
| Informatica | Axon | 7.2.x | Workaround |  | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | Data Privacy Management | 10.5, 10.5.1 | Workaround |  | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | Information Deployment Manager |  | Fix | | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | Metadata Manager | 10.4, 10.4.1, 10.5, 10.5.1 | Workaround |  | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | PowerCenter | 10.5.1 | Workaround | | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | PowerExchange for CDC (Publisher) and Mainframe | 10.5.1 | Workaround | | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | Product 360 | All versions | Workaround  | | [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-Updates-for-Informatica-On-premises-Products) |
| Informatica | Secure Agents (Cloud hosted)| Unknown | Fix | Fixed agents may need to be restarted| [source](https://knowledge.informatica.com/s/article/Apache-Zero-Day-log4j-RCE-Vulnerability-updates-for-Informatica-Cloud-and-Cloud-Hosted-Software) |
| IronNet | All products | All verisons | Investigation | | [source](https://www.ironnet.com/blog/ironnet-security-notifications-related-to-log4j-vulnerability) |
| Ivanti | All products| All versions | Not Vuln | No products are deemed affected at this moment | [source](https://forums.ivanti.com/s/article/CVE-2021-44228-Java-logging-library-log4j-Ivanti-Products-Impact-Mapping) |

### J

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| JFrog | all products | | Not Vuln | | [source](https://twitter.com/jfrog/status/1469385793823199240) |
| Jamf Nation     | Jamf Cloud | Unknown| Fix | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation     | Jamf Pro (hosted on-prem) | < 10.34.1 |  See notes | <10.14 vulnerable, 10.14-10.34 patch, >= 10.34.1 fix | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740) |
| Jamf Nation | Health Care Listener| Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Connect | Unknown | Not Vuln | |[source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Data Policy| Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Infrastructure Manager| Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Now | Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Private Access | Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Protect | Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf School| Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jamf Nation | Jamf Threat Defense| Unknown | Not Vuln | | [source](https://community.jamf.com/t5/jamf-pro/third-party-security-issue/td-p/253740)|
| Jazz/IBM | JazzSM DASH | Unknown | See notes | DASH on WebSphere Application Server requires mitigations | [source](https://www.ibm.com/support/pages/node/6525552) |
| Jenkins | Jenkins CI | Unknown | Not Vuln | Invidivual plugins not developed as part of Jenkins core *may* be vulnerable. | [source](https://www.jenkins.io/blog/2021/12/10/log4j2-rce-CVE-2021-44228/) |
| JetBrains | YouTrack Standalone | >= 2019.2 <= 2021.4.34389| Vuln | email, [mitigation](https://www.jetbrains.com/help/youtrack/standalone/Configure-JVM-Options.html#set-jvm-options-jar) |
| Jetbrains | TeamCity | Unknown | Investigation | | [source](https://youtrack.jetbrains.com/issue/TW-74298) |
| Jitsi | jitsi-videobridge | v2.1-595-g3637fda42 | Fix  | | [source](https://github.com/jitsi/security-advisories/blob/4e1ab58585a8a0593efccce77d5d0e22c5338605/advisories/JSA-2021-0004.md)|
| Juniper Networks | Cross Provisioning Platform | Unspecified | Under investigation | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | JSA Series | Unspecified | Under investigation | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Advanced Threat Prevention (JATP) | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks AppFormix | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Apstra System | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Connectivity Services Director | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Contrail products: Contrail Analytics, Contrail Cloud, Contrail Networking or Contrail Service Orchestration | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks CTPOS and CTPView | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks ICEAAA Manager | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks JATP Cloud | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Juniper Identity Management Services (JIMS) | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Juniper Mist Edge | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Juniper Sky Enterprise | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Junos OS Evolved | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Junos OS | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Mist Access Points | Any version on AP12, AP21, AP32, AP33, AP34, AP41, AP43, AP45, AP61, AP63. | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Network Director | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Policy Enforcer | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks products using Wind River Linux in Junos OS and Junos OS Evolved | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks ScreenOS | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks SecIntel | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Security Director Insights | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Security Director | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Session Smart Router (Formerly 128T) | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Space SDK | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Juniper Networks Standalone Log Collector 20.1 (as also used by Space Security Director) | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Junos Space Network Management Platform  | Unspecified | Vulnerable | Only when OpenNMS has been enabled. | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks Marvis Virtual Network Assistant (VNA) | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks Mist AI | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks Paragon Active Assurance | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks WAN Assurance | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks Wi-Fi Assurance | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | MIST: Juniper Networks Wired Assurance | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Northstar Controller | Unspecified | Vulnerable | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Northstar Planner | Unspecified | Under investigation | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Paragon Insights | >= 21 version 21.1 ; >= 22 version 22.2  | Vulnerable | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Paragon Pathfinder | >= 21 version 21.1 ; >= 22 version 22.2 | Vulnerable | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Paragon Planner | >= 21 version 21.1 ; >= 22 version 22.2 | Vulnerable | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | Secure Analytics | Unspecified | Under investigation | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |
| Juniper Networks | User Engagement Virtual BLE | Unspecified | Not Vuln | | [source](https://kb.juniper.net/InfoCenter/index?page=content&id=JSA11259&actp=SUBSCRIPTION) |

### K

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Kaseya | AuthAnvil | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | BMS | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | ID Agent DarkWeb ID and BullPhish ID | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | IT Glue | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | MyGlue | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Network Glue | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Passly | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | RocketCyber | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Spannign Salesforce Backup | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Spanning O365 Backup | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Unitrends | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | VSA SaaS and VSA On-Premises | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | Vorex | Unknown | Not Vuln | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Kaseya | products not listed above | Unknown | Investigation | | [source](https://helpdesk.kaseya.com/hc/en-gb/articles/4413449967377-Log4j2-Vulnerability-Assessment) |
| Keycloak | Keycloak | all version | Not Vuln | | [source](https://github.com/keycloak/keycloak/discussions/9078) |

### L

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| LeanIX | All products | All versions | Fix | | [source](https://www.leanix.net/en/blog/log4j-vulnerability-log4shell) |
| Lightbend | Akka  | Unknown | Not Vuln| | [source](https://discuss.lightbend.com/t/regarding-the-log4j2-vulnerability-cve-2021-44228/9275) |
| Lightbend | Akka Serverless | Unknown | Not Vuln| | [source](https://discuss.lightbend.com/t/regarding-the-log4j2-vulnerability-cve-2021-44228/9275) |
| Lightbend | Lagom Framework | Unknown | Not Vuln by default | Users that switched from logback to log4j are affected | [source](https://discuss.lightbend.com/t/regarding-the-log4j2-vulnerability-cve-2021-44228/9275) |
| Lightbend | Play Framework| Unknown | Not Vuln by default | Users that switched from logback to log4j are affected | [source](https://discuss.lightbend.com/t/regarding-the-log4j2-vulnerability-cve-2021-44228/9275) |
| LogicMonitor | LogicMonitor SaaS Platform| Unknown | Fix | Automatic update before 13th December [source](https://communities.logicmonitor.com/topic/7472-logicmonitor-collectors-running-vulnerable-version-of-log4j-are-affected-by-log4shell-cve-2021-44228-vulnerability/) |
| The Linux Foundation | XCP-ng | All versions | Not vuln | |[source](https://xcp-ng.org/forum/topic/5315/log4j-vulnerability-impact) |
| LiquidFiles | LiquidFiles | All versions | Not vuln | |[source](https://mailchi.mp/liquidfiles/liquidfiles-log4j) |
| Lyrasis | DSpace | 7.x | Fix/Workaround | |[source](https://groups.google.com/g/dspace-community/c/Fa4VdjiiNyE) |

### M

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Mailcow | Mailcow Solr Docker| < 1.8 | Fix | | [source](https://community.mailcow.email/d/1229-cve-2021-44228-vulnerability-solr) |
| MailStore | MailStore | all | Not Vuln  | | [source](https://www.mailstore.com/en/blog/mailstore-affected-by-log4shell/) |
| ManageEngine | ADAudit Plus | Unknown | Investigation | Third party components bundle log4j | |
| ManageEngine | ADManager Plus | Unknown | Investigation| Mitigation: set `-Dlog4j2.formatMsgNoLookups=true` in `jvm.options`. | [source](https://pitstop.manageengine.com/portal/en/community/topic/log4j-ad-manager-plus) |
| ManageEngine | Desktop Central | Unknown | Not Vuln | |[source](https://pitstop.manageengine.com/portal/en/community/topic/log4j-security-issue) |
| McAfee | Data Exchange Layer (DXL) | Unknown | Not Vuln || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | Enterprise Security Manager (ESM) | 11.x | Workaround || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | McAfee Active Response (MAR) | Unknown | Not Vuln | Standalone MAR not vulnerable, for MAR included in bundle see TIE | [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | Network Security Manager (NSM) | Unknown | Not Vuln || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | Network Security Platform (NSP) | Unknown | Not Vuln || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | Threat Intelligence Exchange (TIE) | 2.2, 2.3, 3.0 | Workaround || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | ePolicy Orchestrator Agent Handlers (ePO-AH) | Unknown | Not Vuln || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | ePolicy Orchestrator Application Server (ePO) | <= 5.10 CU10 | Not Vuln || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| McAfee | ePolicy Orchestrator Application Server (ePO) | 5.10 CU11 | Workaround || [source](https://kc.mcafee.com/corporate/index?page=content&id=KB95091) |
| Memurai | All products | | Not Vuln | | [source](https://www.memurai.com/blog/apache-log4j2-cve-2021-44228) |
| Metabase  | Metabase                         | <0.41.4 | Fix      | Mitigations available for earlier versions                                                                | [source](https://github.com/metabase/metabase/releases/tag/v0.41.4)                                                                                                                                                                                                        |
| Microsoft |                                  |         |          | Microsoft provided additional guidance for preventing, detecting and hunting for exploitation             | [source](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/), [IOCs](https://github.com/Azure/Azure-Sentinel/blob/master/Detections/MultipleDataSources/Log4J_IPIOC_Dec112021.yaml) |
| Microsoft | Azure AD                         | Unknown | Not Vuln | ADFS itself is not vulnerable, federation providers may be                                                | [source](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)                                                                                                                                                                  |
| Microsoft | Azure App Service                | Unknown | Not Vuln | This product itself is not vulnerable, Microsoft provides guidance on remediation for hosted applications | [source](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)                                                                                                                                                                  |
| Microsoft | Azure Application Gateway        | Unknown | Not Vuln |                                                                                                           | [source](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)                                                                                                                                                                  |
| Microsoft | Azure Front Door                 | Unknown | Not Vuln |                                                                                                           | [source](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)                                                                                                                                                                  |
| Microsoft | Azure WAF                        | Unknown | Not Vuln |                                                                                                           | [source](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)                                                                                                                                                                  |
| Microsoft | Kafka Connect for Azure Cosmo DB | < 1.2.1 | Fix      |                                                                                                           | [source](https://github.com/microsoft/kafka-connect-cosmosdb/blob/0f5d0c9dbf2812400bb480d1ff0672dfa6bb56f0/CHANGELOG.md)                                                                                                                                                   |
| Minecraft | Java edition | <1.18.1 | Fix | Mitigations available for earlier versions| [source](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition)
| Mitel      | Mitel Interaction Recording (MIR) | 	6.3 to 6.7 | Fix | see SA211213-17 |[source](https://www.mitel.com/-/media/mitel/file/pdf/support/security-advisories/security-bulletin_21-0010-001.pdf) |
| Mitel      | Mitel MiVoice Business | 	All | Investigation |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      |Mitel MiVoice MX-ONE | 	All | Investigation |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiCollab | 	All | Investigation |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | Open Integration Gateway (OIG) | 	All | Investigation |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | Mitel Performance Analytics Server and Probe | 	All | Investigation |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | Mitel Standard Linux (MSL) | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiVoice 5000 | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiVoice Office 400 | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiVoice Connect | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiVoice Border Gateway | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiContact Center Business | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| Mitel      | MiContact Center  Enterprise | 	All | Not vuln |  |[source](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-21-0010) |
| MISP | MISP | All | Not vuln | |[source](https://twitter.com/MISPProject/status/1470051242038673412) |
| MONARC | MONARC | All | Not vuln | |[source](https://twitter.com/MONARCproject/status/1470349937443491851) |
| MongoDB | Atlas Search | Unknown | Fix | Affected and patched. No evidence of exploitation or indicators of compromise prior to the patch were discovered. | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Atlas | Unknown | Not vuln | Including Atlas Database, Data Lake, Charts | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Enterprise Advanced | Unknown | Not vuln | Including Enterprise Server, Ops Manager, Enterprise Kubernetes Operators. | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Community Edition | Unknown | Not vuln | Including Community Server, Cloud Manager, Community Kubernetes Operators. | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Drivers | Unknown | Not vuln | | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Tools | Unknown | Not vuln | Including Compass, Database Shell, VS Code Plugin, Atlas CLI, Database Connectors | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| MongoDB | Realm | Unknown | Not vuln | including Realm Database, Sync, Functions, APIs | [source](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)
| Moodle | Moodle | All | Not vuln | | [source](https://moodle.org/mod/forum/discuss.php?d=429966)

### N

| Supplier           | Product                                                            | Version  (See Status) |    Status     | Notes                                          |                                                                                                            Links |
|--------------------|--------------------------------------------------------------------|:---------------------:|:-------------:|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------:|
| N-able             | Backup                                                             | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | MSP Manager                                                        | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | Mail Assure                                                        | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | N-central                                                          | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | Passportal                                                         | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | RMM                                                                | Unknown  |      Fix      |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | Risk Intelligence                                                  | Unknown  |  Vulnerable   |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| N-able             | Take Control                                                       | Unknown  |   Not Vuln    |                                                |                                 [source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability) |
| Neo4j              | Neo4j                                                              | > 4.2    |  Vulnerable   | Workaround is available, but not released yet. |                                     [source](https://community.neo4j.com/t/log4j-cve-mitigation-for-neo4j/48856) |
| Nelson             | Nelson                                                             | 0.16.185 |  Vulnerable   | Workaround is available, but not released yet. | [source](https://github.com/getnelson/nelson/blob/f4d3dd1f1d4f8dfef02487f67aefb9c60ab48bf5/project/custom.scala) |
| NetApp             | Brocade SAN Naviator                                               | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | Cloud Manager                                                      | Unknown  |  Vulnerable   |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | Element Plug-in for vCenter Server                                 | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | Management Services for Element Software and NetApp HCI            | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | NetApp HCI Compute Node                                            | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | NetApp SolidFire & HCI Management Node                             | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | NetApp SolidFire Plug-in for vRealize Orchestrator (SolidFire vRO) | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | NetApp SolidFire, Enterprise SDS & HCI Storage                     | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| NetApp             | NetApp SolidFireStorage Replication Adapter                        | Unknown  | Investigation |                                                |                                               [source](https://security.netapp.com/advisory/ntap-20211210-0007/) |
| Netflix            | atlas                                                              |  1.6.6   |  Workaround   |                                                |                       [source](https://github.com/Netflix/atlas/commit/5baff2b656a45886b85968a4b66f33bd36c648be) |
| Netflix            | dgs-framework                                                      | < 4.9.11 |      Fix      |                                                |                                             [fix](https://github.com/Netflix/dgs-framework/releases/tag/v4.9.11) |
| Netflix            | spectator                                                          | < 1.0.9  |      Fix      |                                                |                                                  [fix](https://github.com/Netflix/spectator/releases/tag/v1.0.9) |
| Netflix            | zuul                                                               | Unknown  |  Workaround   |                                                |                        [source](https://github.com/Netflix/zuul/commit/280f20cd51deb7e72275625d5ec556aae06f6a29) |
| NetIQ | Access Manager | > 4.5.x & > 5.0.x | Workaround || [workaround](https://portal.microfocus.com/s/article/KM000002997)|
| Netwrix            | Netwrix Auditor                                                    |          |   Not vuln    |                                                |                                 [source](http://www.publicnow.com/view/EA90CB461F5F0A1BA339E2AC55C719CA5AD58CE4) |
| New Relic          | Java Agent                                                         |  6.5.1 & 7.4.1  |      Fix      |                                                |                                             [source](https://docs.newrelic.com/docs/security/new-relic-security/security-bulletins/security-bulletin-nr21-03/) |
| NextGen Healthcare | Mirth                                                              | Unknown  |   Not Vuln    |                                                |                [source](https://github.com/nextgenhealthcare/connect/discussions/4892#discussioncomment-1789526) |
| NSA | Ghidra| < 10.1| Fix | | [source](https://github.com/NationalSecurityAgency/ghidra/blob/2c73c72f0ba2720c6627be4005a721a5ebd64b46/README.md#warning), [fix](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_10.1_build)|
| Nutanix | AOS | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | AHV | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Prism Central | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Flow Security Central | All versions | Unknown |  | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Files | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Objects | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Volumes | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Mine | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Era | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | X-Ray | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | LCM | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Move | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | NCC | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Foundation | All versions | Unknown | Investigating | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Karbon | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Leap | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Calm | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Beam | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Frame | All versions | Not Vuln | | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Sizer | Unknown | Fix | See advisory | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| Nutanix | Insights | All versions | Vulnerable | Patch pending | [source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
| NXLog | NXLog Manager |  5.x | Not Vuln | | [source](https://nxlog.co/news/apache-log4j-vulnerability-cve-2021-44228)|

### O

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Obsidian Dynamics | kafdrop | all | Investigation | | [source](https://github.com/obsidiandynamics/kafdrop/issues/315) |
| Okta       | AD Agent                                           | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | Access Gateway                                     | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | Advanced Server Access                             | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | Browser Plugin                                     | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | IWA Web Agent                                      | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | LDAP Agent                                         | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | Mobile                                             | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | On-Prem MFA Agent                                  | <1.4.6                           | Fix        |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell), [fix](https://trust.okta.com/security-advisories/okta-on-prem-mfa-agent-cve-2021-44228)                |
| Okta       | Radius Server Agent                                | 2.17.0                           | Fix        |                                                    | [source/fix](https://trust.okta.com/security-advisories/okta-radius-server-agent-cve-2021-44228)                |
| Okta       | Verify                                             | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta       | Workflow                                           | Unknown                          | Not Vuln   |                                                    | [source](https://sec.okta.com/articles/2021/12/log4shell)                                                                                                         |
| Okta | RADIUS Server Agent | <2.17.0 | Fix|| [source](https://sec.okta.com/articles/2021/12/log4shell), [fix](https://trust.okta.com/security-advisories/okta-radius-server-agent-cve-2021-44228) |
| OpenMRS    | Talk                                               | 2.4.0-2.4.1                      | Vulnerable | Mitigations are available, pending a new release   | [source](https://talk.openmrs.org/t/urgent-security-advisory-2021-12-11-re-apache-log4j-2/35341)                                                                  |
| OpenNMS    | Horizon (including derived Sentinels)              | < 29.0.3                         | Fix        | Workarounds are available too for earlier versions | [source](https://www.opennms.com/en/blog/2021-12-10-opennms-products-affected-by-apache-log4j-vulnerability-cve-2021-44228/)                                      |
| OpenNMS    | Meridian (including derived Minions and Sentinels) | < 2021.1.8, 2020.1.15, 2019.1.27 | Fix        | Workarounds are available too for earlier versions | [source](https://www.opennms.com/en/blog/2021-12-10-opennms-products-affected-by-apache-log4j-vulnerability-cve-2021-44228/)                                      |
| OpenNMS    | Minion appliance                                   | Unknown                          | Fix        |                                                    | [source](https://www.opennms.com/en/blog/2021-12-10-opennms-products-affected-by-apache-log4j-vulnerability-cve-2021-44228/)                                      |
| OpenNMS    | PoweredBy OpenNMS                                  | Unknown                          | Workaround |                                                    | [source](https://www.opennms.com/en/blog/2021-12-10-opennms-products-affected-by-apache-log4j-vulnerability-cve-2021-44228/)                                      |
| OpenSearch | OpenSearch                                         | < 1.2.1                          | Fix        |                                                    | [source](https://opensearch.org/blog/releases/2021/12/update-to-1-2-1/)                                                                                           |
| Oracle     | Database                                           | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Fusion Middleware                                  | Unknown                          | Fix        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 209768.1](https://support.oracle.com/rs?type=doc&id=209768.1), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | NoSQL Database                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle Access Manager                          | Unknown                          | Vulnerable        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle Data Integrator (ODI)                          | >= 12.2.1.3.210119, Marketplace - >= 2.1.0                          | Workaround        |[Patch Available, Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1), Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)           |
| Oracle     | Oracle eBusiness Suite                          | Unknown                          | Workaround        |[MOS note 2827804.1](https://support.oracle.com/rs?type=doc&id=2827804.1)                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle Enterprise Manager                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 209768.1](https://support.oracle.com/rs?type=doc&id=209768.1), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle Enterprise Repository                          | Unknown                          | Workaround        |[Mitigation, Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1), Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)           |
| Oracle     | Oracle Fusion Middleware Infrastructure                          | Unknown                          | Vulnerable        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle HTTP Server                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 209768.1](https://support.oracle.com/rs?type=doc&id=209768.1), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle Internet Directory                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 209768.1](https://support.oracle.com/rs?type=doc&id=209768.1), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle JDeveloper                          | Unknown                          | Workaround        |[Mitigation Available, Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1), Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)           |
| Oracle     | Oracle Policy Automation (OPA)                          | Unknown                          | Vulnerable        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle SOA Suite                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle WebCenter Portal                          | 12.2.1.3 & 12.2.1.4 | Workaround        |  [MOS note 2827977.1](https://support.oracle.com/rs?type=doc&id=2827977.1) using Elasticsearch which uses Log4j 2.X jars  | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| Oracle     | Oracle WebCenter Sites                          | Unknown                          | Workaround        |[Mitigation Available, Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1), Support Note 2827793.1] (https://support.oracle.com/rs?type=doc&id=2827793.1)           |
| Oracle     | Oracle WebLogic Server                          | Unknown                          | Not Vuln        |                                                    | [source](https://www.oracle.com/security-alerts/alert-cve-2021-44228.html), [Support note 209768.1](https://support.oracle.com/rs?type=doc&id=209768.1), [Support note 2827611.1](https://support.oracle.com/rs?type=doc&id=2827611.1)           |
| openHAB    | openHAB                                            | 3.0.4, 3.1.1                          | Fix |            | [source](https://github.com/openhab/openhab-distro/security/advisories/GHSA-j99j-qp89-pcfq) |
| OTRS      | All products                                                |                        | Not Vuln      |                                                    | [source](https://portal.otrs.com/external) |
| OWASP      | ZAP                                                | < 2.11.1                         | Fix        |                                                    | [source](https://www.zaproxy.org/blog/2021-12-10-zap-and-log4shell/) |

### P

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| PagerDuty | Rundeck | 3.3+ | Fix | No statement from PagerDuty yet. | [source](https://github.com/rundeck/rundeck/pull/7427) |
| Palo Alto | WildFire Appliance | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | Prisma Cloud Compute | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | Prisma Cloud  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | PAN-OS  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | GlobalProtect App  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | Cortex XSOAR  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | Cortex XDR Agent  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | CloudGenix  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| Palo Alto | Bridgecrew  | | Not Vuln | | [source](https://security.paloaltonetworks.com/CVE-2021-44228) |
| PaperCut  | PaperCut MF | >= 21.0 | Workaround | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut NG | >= 21.0 | Workaround | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut Hive | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut Pocket | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut Views | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut Print Logger | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut MobilityPrint | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut MultiVerse | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| PaperCut  | PaperCut Online Services | | Not vuln | |[source](https://www.papercut.com/kb/Main/Log4Shell-CVE-2021-44228) |
| Parallels | Remote Application Server  | All versions | Not Vuln | | [source](https://kb.parallels.com/en/128696) |
| Pega | Pega Platform | On Prem | Fix | | [source](https://docs.pega.com/security-advisory/security-advisory-apache-log4j-zero-day-vulnerability) |
| Planon Software | Planon Universe | all | Not vuln | | [source](https://my.planonsoftware.com/uk/news/log4j-impact-on-planon/) |
| Plex | Industrial IoT | | Not vuln | Mitigation already applied, patch will be issued today | [source](https://rockwellautomation.custhelp.com/app/answers/answer_view/a_id/1133605) |
| Postgres | PostgreSQL JDBC | | Not vuln | | [source](https://www.postgresql.org/about/news/postgresql-jdbc-and-the-log4j-cve-2371/) |
| Progress | OpenEdge | | Workaround | | [source](https://www.progress.com/security), [mitigations](https://knowledgebase.progress.com/articles/Knowledge/Is-OpenEdge-vulnerable-to-CVE-2021-44228-Log4j) |
| Progress | DataDirect Hybrid Data Pipeline | | Workaround | | [source](https://www.progress.com/security), [mitigations](https://knowledgebase.progress.com/articles/Knowledge/Is-Hybrid-Data-Pipeline-vulnerable-CVE-2021-44228-Log4j) |
| Portex | Portex | <3.0.2 | Fix | | [source](https://github.com/katjahahn/PortEx/releases)|
| Pulse Secure | Pulse Secure Virtual Traffic Manager | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Secure Services Director | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Secure Web Application Firewall | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Connect Secure | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Ivanti Connect Secure (ICS) | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Policy Secure | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Desktop Client | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse Mobile Client | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse One | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Pulse ZTA | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Ivanti Neurons for ZTA | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Pulse Secure | Ivanti Neurons for secure Access | | Not Vuln | | [source](https://kb.pulsesecure.net/articles/Pulse_Secure_Article/KB44933/) |
| Puppet | Continuous Delivery for Puppet Enterprise | 3.x, < 4.10.2| Fix | Update available for version 4.x, mitigations for 3.x which is EOL| [source](https://puppet.com/blog/puppet-response-to-remote-code-execution-vulnerability-cve-2021-44228/), [workaround](https://puppet.com/docs/continuous-delivery/4.x/cd_release_notes.html#cd_release_notes-version-4-10-3),[mitigations](https://support.puppet.com/hc/en-us/articles/360046708133-Puppet-Response-to-CVE-2021-44228-FAQ/) |
| Puppet | Puppet agents | | Not Vuln | | [source](https://puppet.com/blog/puppet-response-to-remote-code-execution-vulnerability-cve-2021-44228/) |
| Puppet | Puppet Enterprise| | Not Vuln | | [source](https://puppet.com/blog/puppet-response-to-remote-code-execution-vulnerability-cve-2021-44228/) |
| PTV xServer internet 1 / PTV xServer internet 2 | PTV xServer internet 1 / PTV xServer internet 2 | Unknown | Fix           |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV TLN planner internet                        | PTV TLN planner internet                        | Unknown | Fix           |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Route Optimizer SaaS / Demonstrator         | PTV Route Optimizer SaaS / Demonstrator         | Unknown | Fix           |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Developer                                   | PTV Developer                                   | Unknown | Fix           |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Visum Publisher                             | PTV Visum Publisher                             | Unknown | Fix           |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV xServer 2.x (on prem)                       | PTV xServer 2.x (on prem)                       | Unknown | Vulnerable    |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV xServer 1.34 (on prem)                      | PTV xServer 1.34 (on prem)                      | Unknown | Vulnerable    |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV MaaS Modeller                               | PTV MaaS Modeller                               | Unknown | Vulnerable    |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Route Optimiser CL                          | PTV Route Optimiser CL                          | Unknown | Investigation |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Route Optimiser ST                          | PTV Route Optimiser ST                          | Unknown | Investigation |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Map&Market                                  | PTV Map&Market                                  | Unknown | Investigation |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Arrival Board / Trip Creator / EM Portal    | PTV Arrival Board / Trip Creator / EM Portal    | Unknown | Investigation |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Drive&Arrive                                | PTV Drive&Arrive                                | Unknown | Investigation |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV xServer < 1.34 (on prem)                    | PTV xServer < 1.34 (on prem)                    | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Road Editor                                 | PTV Road Editor                                 | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Map&Guide internet                          | PTV Map&Guide internet                          | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Map&Guide intranet                          | PTV Map&Guide intranet                          | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Navigator Licence Manager                   | PTV Navigator Licence Manager                   | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Navigator App                               | PTV Navigator App                               | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Drive&Arrive App                            | PTV Drive&Arrive App                            | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Visum                                       | PTV Visum                                       | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Vissim                                      | PTV Vissim                                      | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Vistro                                      | PTV Vistro                                      | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Viswalk                                     | PTV Viswalk                                     | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Balance and PTV Epics                       | PTV Balance and PTV Epics                       | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Hyperpath                                   | PTV Hyperpath                                   | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV TRE and PTV Tre-Addin                       | PTV TRE and PTV Tre-Addin                       | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| PTV Optima                                      | PTV Optima                                      | Unknown | Not vuln      |       | [source](https://company.ptvgroup.com/en/resources/service-support/log4j-latest-information) |
| Pyramid Analytics                               | Pyramid Analytics                               | All     | Not vuln      |       | [source](https://community.pyramidanalytics.com/t/83hjjt4/log4j-security-vulnerability-pyramid) |

### Q

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| QlikTech International | Compose | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Nprinting | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | QEM products | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Qlik Replicate | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Qlik Sense Enterprise | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | QlikView | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QOS.ch          | SLF4J Simple Logging Facade for Java | |  | SLF4J API doesn't protect against the vulnerability when using a vulnerable version of log4j | [source](http://slf4j.org/log4shell.html) |

### R

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Red Hat         | Red Hat OpenShift Container Platform 4 openshift4/ose-metering-presto |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 4 openshift4/ose-metering-hive |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 4 openshift4/ose-logging-elasticsearch6 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 3.11 openshift3/ose-logging-elasticsearch5 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenStack Platform 13 (Queens) opendaylight |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Logging logging-elasticsearch6-container |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat build of Quarkus |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Descision Manager 7 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat JBoss Enterprise Application Platform Expansion Pack |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Process Automation 7 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | A-MQ Clients 2 |  | Not Vuln | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat CodeReady Studio 12 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Data Grid 8 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Integration Camel K |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Integration Camel Quarkus |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat JBoss A-MQ Streaming |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat JBoss Fuse 7 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Application Runtimes |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat Single Sign-On 7 |  | Not Vuln | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat JBoss Enterprise Application Platform 6 |  | Not Vuln | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Redis | Redis Enterprise & Open Source | all | Not Vuln | Redis Enterprise and Open Source Redis (self-managed software product) does not use Java and is therefore not impacted by this vulnerability | [source](https://redis.com/security/notice-apache-log4j2-cve-2021-44228/) |
| RSA             | SecurID Authentication Manager |  | Not Vuln | Version 8.6 Patch 1 contains a version of log4j that is vulnerable, but this vulnerability is not exploitable. | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| Riverbed        | SteelHead CX (appliance, virtual, cloud) | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | SteelHead Interceptor | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | SteelCentral Controller for SteelHead | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | Client Accelerator Controllers and Client Accelerator (aka SteelCentral Controller for SteelHead Mobile and SteelHead Mobile) | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | SteelCentral Controller for SteelHead | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | WinSec Controller for SteelHead (WSC) | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | SaaS Accelerator | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | AppResponse11 | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| Riverbed        | Packet Analyzer | Not Vuln | | [source](https://supportkb.riverbed.com/support/index?page=content&id=S35645&actp=LIST_RECENT) |
| RSA             | SecurID Authentication Manager Prime |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Authentication Manager WebTier |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Identity Router (On-Prem component of Cloud Authentication Service) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Governance and Lifecycle (SecurID G&L) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Governance and Lifecycle Cloud (SecurID G&L Cloud) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |

### S

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Safe            | FME Server      | | Investigation | | [source](https://community.safe.com/s/article/Is-FME-Server-Affected-by-the-Security-Vulnerability-Reported-Against-log4j) |
| Salesforce      | All products    | | Investigation | | [source](https://status.salesforce.com/generalmessages/826) | 
| SAP             | XS Advanced Runtime | 1.0.140 or lower | Fix | SAP note 3130698 | https://launchpad.support.sap.com/#/notes/3130698 |
| SAP             | Customer Checkout PoS / manager | 2.0 FP09, 2.0 FP10, 2.0 FP11 PL06 (or lower) and 2.0 FP12 PL04 (or lower) | Fix | SAP note 3130499 | https://launchpad.support.sap.com/#/notes/0003130499 |
| SAS Institute   | JMP | | Not vuln | | [source](https://support.sas.com/content/support/en/security-bulletins/remote-code-execution-vulnerability-cve-2021-44228.html) |
| SAS Institute   | SAS Profile | | Fix | | [source](https://support.sas.com/content/support/en/security-bulletins/remote-code-execution-vulnerability-cve-2021-44228.html) |
| SAS Institute   | SAS Cloud Solutions | | Workaround | | [source](https://support.sas.com/content/support/en/security-bulletins/remote-code-execution-vulnerability-cve-2021-44228.html) |
| Schneider Electric | All products  |  | Investigation | | [source](https://download.schneider-electric.com/files?p_Doc_Ref=SESB-2021-347-01) |
| Security Onion Solutions | Security Onion | 2.3.90 20211210 | Fix | | [source](https://blog.securityonion.net/2021/12/security-onion-2390-20211210-hotfix-now.html) |
| Shibboleth      | Shibboleth IdP/SP | | Not Vuln |  | [source](https://shibboleth.net/pipermail/announce/2021-December/000253.html) |
| Siemens     | Capital (and its derivatives) | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Comos Desktop App | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | E-Car OC Cloud Application | | Fix | Vulnerability fixed on central cloud service starting2021-12-13; no user actions necessary | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | EnergyIP | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | EnergyIP Prepay | 3.7, 3.8 | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Geolus | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | HCRA | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | HES UDIS | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Industrial Edge Management App (IEM-App) | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Industrial Edge Management OS (IEM-OS) | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Industrial Edge Manangement Hub | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | LOGO! Soft Comfort | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Mendix Applications | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Mindsphere Cloud Application | | Fix | Vulnerability fixed on central cloud service starting2021-12-11; no user actions necessary | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Operation Scheduler |  >= V1.1.3 | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | RUGGEDCOM ELAN | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | RUGGEDCOM MAESTRO | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SIGUARD DSA | V4.2, V4.3, V4.4 | Workaround | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SIMATIC WinCC V7.4 | V7.4 SP1 | Fix | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SINAMICS TEC - SDK | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SINUMERIK Analyze MyWorkpiece / Capture | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SINUMERIK Optimize MyMachine | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SiPass Integrated | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Siveillance Command |  >= 4.16.2.1 | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Siveillance Control Pro | < V2.1 | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Siveillance Control Pro | >= V2.1 | Workaround | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Siveillance Vantage | all | Vulnerable | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | SIZER Design Tool for SINAMICS | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Spectrum Power | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Solid Edge | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Solid Edge Technical Publication | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Solid Edge Wiring and Harness Design | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | Teamcenter | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| Siemens     | XHQ | | Investigation | | [source](https://cert-portal.siemens.com/productcert/pdf/ssa-661247.pdf) |
| SolarWinds      | Database Performance Analyzer | 2021.1.x, 2021.3.x, 2022.1.x | Workaround | | [source](https://www.solarwinds.com/trust-center/security-advisories/cve-2021-44228), [workaround](https://support.solarwinds.com/SuccessCenter/s/article/Database-Performance-Analyzer-DPA-and-the-Apache-Log4j-Vulnerability-CVE-2021-44228?language=en_US) |
| SolarWinds      | Server & Application Monitor | >= 2020.2.6 | Workaround | | [source](https://www.solarwinds.com/trust-center/security-advisories/cve-2021-44228), [workaround](https://support.solarwinds.com/SuccessCenter/s/article/Server-Application-Monitor-SAM-and-the-Apache-Log4j-Vulnerability-CVE-2021-44228?language=en_US) |
| SolarWinds      | Orion Platform core | | Not vuln | | [source](https://www.solarwinds.com/trust-center/security-advisories/cve-2021-44228) |
| SonarSource     | SonarQube | | Workaround | | [source](https://community.sonarsource.com/t/sonarqube-sonarcloud-and-the-log4j-vulnerability/54721) |
| SonarSource     | SonarCloud |  | Fix | | [source](https://community.sonarsource.com/t/sonarqube-sonarcloud-and-the-log4j-vulnerability/54721) |
| SonicWall       | Gen5 Firewalls (EOS) |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Gen6 Firewalls |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Gen7 Firewalls |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SonicWall Switch |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SMA 100 |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SMA 1000 | 12.1.0, 12.4.1 | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Email Security | 10.x | Vulnerable | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | MSW |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | NSM |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Analyzer |  | Investigation | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Analytics |  | Investigation | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | GMS |  | Investigation | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Capture Client & Capture Client Portal |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | CAS |  | Investigation | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | WAF |  | Investigation | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Access Points |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | WNM |  | Not Vuln | |  [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Capture Security Appliance  |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | WXA |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SonicCore |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| Sophos          | Sophos Central |  | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Sophos Firewall | All | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | SG UTM | All | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | SG UTM Manager (SUM)  | All | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Sophos ZTNA |  | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Cloud Optix |  | Fix | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Sophos Home |  | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Sophos Mobile |  | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Sophos Mobile EAS Proxy | 9.7.2 | Fix | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Sophos          | Reflexion |  | Not Vuln | | [source](https://www.sophos.com/en-us/security-advisories/sophos-sa-20211210-log4j-rce) |
| Splunk          | Add-On: Java Management Extensions | 3.0.0, 2.1.0 | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Add-On: JBoss | 3.0.0, 2.1.0 | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Add-On: Tomcat | 3.0.0, 2.1.0 | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Data Stream Processor | DSP 1.0.x, DSP 1.1.x, DSP 1.2.x | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | IT Service Intelligence (ITSI) | 4.11.x, 4.10.x, 4.9.x, 4.8.x, 4.7.x, 4.4.x | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Connect for Kafka | <2.0.4 | Fix | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Enterprise | All supported non-Windows versions of 8.1.x and 8.2.x only if Hadoop (Hunk) and/or DFS are used. | Workaround | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Enterprise Amazon Machine Image (AMI) | see Splunk Enterprise | Workaround | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Enterprise Docker Container | see Splunk Enterprise | Workaround | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Logging Library for Java | <1.11.1 | Fix | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Stream Processor Service | Current | Vulnerable | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Admin Config Service | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Analytics Workspace | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Behavior Analytics | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Dashboard Studio | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Developer Tools: AppInspect | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Enterprise Security | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Intelligence Management (TruSTAR) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | KV Service | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Mission Control | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | MLTK | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Operator for Kubernetes | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Security Analytics for AWS | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | SignalFx Smart Agent | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | SOAR Cloud (Phantom) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | SOAR (On-Premises) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Application Performance Monitoring | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Augmented Reality | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Cloud Data Manager (SCDM) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Connect for Kubernetes | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Connect for SNMP | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Connect for Syslog | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk DB Connect | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Enterprise Cloud | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Heavyweight Forwarder (HWF) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Infrastructure Monitoring | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Log Observer | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Mint | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Mobile | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Network Performance Monitoring | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk On-Call/Victor Ops | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Open Telemetry Distributions | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Profiling | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Real User Monitoring | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Secure Gateway (Spacebridge) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Synthetics | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk TV | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk Universal Forwarder (UF) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Splunk          | Splunk User Behavior Analytics (UBA) | all | Not vuln | | [source](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html) |
| Stardog | Stardog | <7.8.1 | Fix | | [source](https://community.stardog.com/t/stardog-7-8-1-available/3411) |
| Stratodesk | NoTouch | 4.5.231 | Fix | | http://cdn.stratodesk.com/repository/notouch-center/10/4.5.231/0/ReleaseNotes-Stratodesk-NoTouch_Center-4.5.231.html |
| Synacor | Zimbra | 8.8.15 and 9.x | Not vuln | Zimbra stated (in their private support portal) they're not vulnerable. Currently supported Zimbra versions ship 1.2.6 |[source](https://forums.zimbra.org/viewtopic.php?f=15&t=70240&start=10#p303354) |
| Sumo logic | Sumu logic | 19.361-12 | Fix | | [source](https://help.sumologic.com/Release-Notes/Collector-Release-Notes#december-11-2021-19-361-12) |
| SUSE | SUSE Linux Enterprise server | all | Not vuln | | [source](https://www.suse.com/c/suse-statement-on-log4j-log4shell-cve-2021-44228-vulnerability/)|
| SUSE | SUSE Rancher | all | Not vuln | | [source](https://www.suse.com/c/suse-statement-on-log4j-log4shell-cve-2021-44228-vulnerability/)|
| SUSE | SUSE Manager | all | Not vuln | | [source](https://www.suse.com/c/suse-statement-on-log4j-log4shell-cve-2021-44228-vulnerability/)|
| SUSE | SUSE Openstack Cloud | all | Vuln | will get update | [source](https://www.suse.com/c/suse-statement-on-log4j-log4shell-cve-2021-44228-vulnerability/)|
| Synology | DSM | | Not vuln | The base DSM is not affected. Software installed via the package manager may be vulnerable. | [source](https://www.synology.com/en-global/security/advisory/Synology_SA_21_30) |
| SysAid | All products | | Fix | | [source](https://www.sysaid.com/lp/important-update-regarding-apache-log4j) |

### T

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
|Tableau | Tableau Server | 2021.2.5| Investigation | | [source](https://www.tableau.com/support/releases/server/2021.2.5)
|Tableau | Tableau Desktop | 2021.4| Investigation | | [source](https://www.tableau.com/support/releases/desktop/2021.4)
| Talend | Talend Component Kit | | Fix | |[source](https://jira.talendforge.org/browse/TCOMP-2054) |
| Tanium | All products | all | Not vuln | | [source](https://community.tanium.com/s/article/How-Tanium-Can-Help-with-CVE-2021-44228-Log4Shell#_Toc90296319)
| Tealium | All products | | Fix | |[source](https://community.tealiumiq.com/t5/Announcements-Blog/Update-on-Log4j-Security-Vulnerability/ba-p/36824) |
| Teamviewer  | All products | | Fix | Server-side hotfix deployed. No user interaction required | [source](https://www.teamviewer.com/en-us/trust-center/security-bulletins/hotfix-log4j2-issue/)|
| TheHive | Cortex | all | Not vuln | |[source](https://blog.strangebee.com/apache-log4j-cve-2021-44228/) |
| TheHive | TheHive | all | Not vuln | |[source](https://blog.strangebee.com/apache-log4j-cve-2021-44228/) |
| Topicus Security | Topicus KeyHub | all | Not vuln | | [source](https://blog.topicus-keyhub.com/topicus-keyhub-is-not-vulnerable-to-cve-2021-44228/) |
| TrendMicro | ActiveUpdate  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Apex Central (including as a Service)  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Apex One (all versions including Mac and Saas)  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud App Security  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud Edge  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Application Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Common Services  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Conformity  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Container Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - File Storage Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Network Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud One - Workload Secuity  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Cloud Sandbox  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Advisor  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Analyzer  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Director  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Email Inspector  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Inspector  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Discovery Web Inspector  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Deep Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Endpoint Application Control  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Fraudbuster  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Home Network Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Housecall  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Instant Messaging Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Internet Security for Mac (Consumer)  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Interscan Messaging Security  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Interscan Messaging Security Virtual Appliance (IMSVA)  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Interscan Web Security Suite  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Interscan Web Security Virtual Appliance (IWSVA)  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Mobile Secuirty for Enterprise  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | MyAccount (Consumer Sign-on)  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Network Viruswall  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | OfficeScan  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Password Manager  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Phish Insight  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Policy Manager  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Portable Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | PortalProtect  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Remote Manager  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Rescue Disk  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Rootkit Buster  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Safe Lock  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Safe Lock 2.0  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Sandbox as a Service  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | ScanMail for Domino  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | ScanMail for Exchange  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Secuirty for Mac  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Security for NAS  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | ServerProtect (all versions)  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Smart Home Network  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Smart Protection Complete  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Smart Protection for Endpoints  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Smart Protection Server (SPS)  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | TippingPoint (all variations)  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | TMUSB  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Trend Micro Email Security & HES  |  | Fix | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Trend Micro ID Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Trend Micro Remote Manager  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Trend Micro Web Security  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Vision One  |  | Fix | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Vulnerability Protection  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Worry-Free Business Security (on-prem)  |  | Investigation | |[source](https://success.trendmicro.com/solution/000289940) |
| TrendMicro | Worry-Free Business Security Services  |  | Not vuln | |[source](https://success.trendmicro.com/solution/000289940) |

### U

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Ubiquiti | UniFi Network Application | 6.5.54 | Fix | |[source](https://community.ui.com/releases/Security-Advisory-Bulletin-023-023/808a1db0-5f8e-4b91-9097-9822f3f90207) |
| US Signal       | Remote Management and Monitoring platform | | Workaround | |[source](https://ussignal.com/blog/apache-log4j-vulnerability) |
| USoft | USoft | 9.1.1F | Vulnerable | Found by manual scanning | [proof](<https://ibb.co/tqV40qB>) |

### V

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Veeam        | All products  | | Not vuln |  | [source](https://www.veeam.com/kb4254)|
| VMware       | API Portal for VMware Tanzu  | 1.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | AppDefense Appliance | 2.x | Workaround |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-AppDefense/ta-p/109180)|
| VMware       | App Metrics  | 2.1.1 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/apm) |
| VMware       | Carbon Black Cloud Workload Appliance | 1.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-Cloud/ta-p/109167) |
| VMware       | Carbon Black EDR Server  | 7.x, 6.x | Fix | Fixed in 7.6.0 | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-EDR/ta-p/109168), [fix](https://community.carbonblack.com/t5/Endpoint-Detection-and-Response/VMware-Carbon-Black-EDR-Announcing-General-Availability-of-EDR/td-p/109189) |
| VMware       | Cloud Foundation  | 4.x, 3.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://kb.vmware.com/s/article/87095)|
| VMware       | Cloud Gateway for VMware Tanzu  | 1.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Cloud Services for VMware Tanzu  | 3.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | HCX | 4.x, 3.x | Vulnerable |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)
| VMware       | Healthwatch for Tanzu Application Service  | 2.1.7, 1.8.6 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/p-healthwatch) |
| VMware       | Horizon | 8.x, 7.x | Workaround |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87073) |
| VMware       | Horizon Cloud Connector | 1.x, 2.x | Fix |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [fix](https://customerconnect.vmware.com/downloads/details?downloadGroup=HCS-CC-210&productId=716&rPId=79131#product_downloads)|
| VMware       | Horizon DaaS | 9.1.x, 9.0.x | Workaround |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87101)|
| VMware       | Identity Manager    | 3.3.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87093) |
| VMware       | NSX Data Center for vSphere | 6.x | Workaround |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87099)|
| VMware       | NSX-T Data Center  | 3.x, 2.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87086) |
| VMware       | Single Sign-On for VMware Tanzu Application Service  | 1.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Site Recovery Manager   | 8.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87098)|
| VMware       | Spring Boot  | < 2.5.8, < 2.6.2 | Workaround |   | [source](https://spring.io/blog/2021/12/10/log4j2-vulnerability-and-spring-boot) |
| VMware       | Spring Cloud Gateway for Kubernetes  | 1.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Tanzu Application Service for VMs  | 2.x | Fix |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US), [fix](https://network.pivotal.io/products/elastic-runtime) |
| VMware       | Tanzu GemFire   | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-all-GemFire-versions?language=en_US)|
| VMware       | Tanzu Greenplum  | 6.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-All-Greenplum-Versions?language=en_US)|
| VMware       | Tanzu Kubernetes Grid Integrated Edition   | 2.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US) |
| VMware       | Tanzu Observability by Wavefront Nozzle   | 3.0.3 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/wavefront-nozzle) |
| VMware       | Tanzu Operations Manager  | 2.x | Fix |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://community.pivotal.io/s/article/5004y00001mPn2N1639255611105?language=en_US), [fix](https://network.pivotal.io/products/ops-manager/) |
| VMware       | Tanzu SQL with MySQL for VMs  | 2.x, 1.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068)|
| VMware       | Telco Cloud Automation | 2.x, 1.x | Vulnerable |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | Unified Access Gateway  | 21.x, 20.x, 3.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87092) |
| VMware       | vCenter Cloud Gateway  | 1.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://kb.vmware.com/s/article/87081)|
| VMware       | vCenter Server  | 6.x | Workaround |  Running on: Windows | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87096?lang=en_US)|
| VMware       | vCenter Server  | 7.x, 6.x | Workaround |  Running on: Virtual Appliance | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87081?lang=en_US) |
| VMware       | vCloud Director | all | Not vuln | | [source](https://kb.vmware.com/s/article/87068?lang=en_US)
| VMware       | vCloud Workstation | all | Not vuln | | [source](https://kb.vmware.com/s/article/87068?lang=en_US)
| VMware       | vRealize Automation     | 8.x, 7.x | Vulnerable |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | vRealize Lifecycle Manager  | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87097)|
| VMware       | vRealize Log Insight     | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87089) |
| VMware       | vRealize Operations    | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87076) |
| VMware       | vRealize Operations Cloud Proxy     | Any | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87080) |
| VMware       | vRealize Orchestrator   | 8.x, 7.x | Vulnerable |   | [source](https://kb.vmware.com/s/article/87068)|
| VMware       | vSphere ESXi | Unknown | Not Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Workspace ONE Access   | 21.x, 20.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [workaround](https://kb.vmware.com/s/article/87090) |
| VMware       | Workspace ONE Access Connector (VMware Identity Manager Connector)  | 19.03.0.1, 20.x, 21.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [workaround](https://kb.vmware.com/s/article/87091)|

### W

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Watcher           | [Watcher](https://github.com/thalesgroup-cert/Watcher) | all | Not vuln | | [source](https://twitter.com/felix_hrn/status/1470387338001977344)
| Wind River      | Wind River Linux | <= 8 | Not vuln | "contain package log4j, but their version is 1.2.x, too old to be affected"  | [source](https://support2.windriver.com/index.php?page=security-notices&on=view&id=7191)|
| Wind River      | Wind River Linux | > 8 | Not vuln  | no support for log4j | [source](https://support2.windriver.com/index.php?page=security-notices&on=view&id=7191)|
| WitFoo          | WitFoo Precinct | 6.x             | Fix             | WitFoo Streamer & Apache Kafka Docker containers are/were vulnerable | [source](https://www.witfoo.com/blog/emergency-update-for-cve-2021-44228-log4j/)|
| Wowza | Wowza Streaming Engine | 4.7.8, 4.8.x | Workaround | |[source](https://www.wowza.com/docs/known-issues-with-wowza-streaming-engine#log4j2-cve) |

### X

### Y

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links      |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Yahoo           | Vespa           |                 | Not vuln        | Your Vespa application may still be affected if log4j is included in your application package |[source](https://blog.vespa.ai/log4j-vulnerability/) |

### Z

| Supplier        | Product         | Version (see Status) | Status          | Notes           | Links      |
|:----------------|:----------------|:--------------------:|:---------------:|:----------------|-----------:|
| Zabbix          | Zabbix          |                 | Not vuln        | Zabbix is aware of this vulnerability, has completed verification, and can conclude that the only product where we use Java is Zabbix Java Gateway, which does not utilize the log4j library, thereby is not impacted by this vulnerability. |[source](https://blog.zabbix.com/zabbix-not-affected-by-the-log4j-exploit/17873/) |
| Zammad          | Zammad          |                 | Workaround      | Most of Zammad instances make use of Elasticsearch which might be vulnerable. |[source](https://community.zammad.org/t/cve-2021-44228-elasticsearch-users-be-aware/8256) |
| Zerto           | Virtual Replication Appliance   | | Not vuln        | |[source](https://help.zerto.com/kb/000004822) |
| Zerto           | Zerto Cloud Appliance |           | Not vuln        | |[source](https://help.zerto.com/kb/000004822) |
| Zerto           | Zerto Cloud Manager |             | Not vuln        | |[source](https://help.zerto.com/kb/000004822) |
| Zerto           | Zerto Virtual Manager |           | Not vuln        | |[source](https://help.zerto.com/kb/000004822) |
| Zesty           | Zesty.io        |                 | Not vuln        | |[source](https://www.zesty.io/mindshare/company-announcements/log4j-exploit/) |
