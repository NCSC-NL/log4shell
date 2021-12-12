# Log4j overview related software

This page contains an overview of any related software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known vulnerable and not vulnerable software. Futhermore any reference to the software will contain specific information regarding which version contains the security fixes, and which software still requires mitigation.

NCSC-NL will use the following status 

| Status         | Description                  |
|:---------------|:-----------------------------|
| Vulnerable     | Software is vulnerable for CVE-2021-44228. |
| Fix            | Software contains a fix for CVE-2021-44228 |
| Workaround | Software is vulnerable but mitigation steps are available |
| Not vuln     | Software is **NOT** vulnerable for CVE-2021-44228. |
| Investigation     | Software is under investigation whether it is vulnerable or not |


## Software overview

### A

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| Apache        | Druid | 0.22.1 | Fix | |[source](https://github.com/apache/druid/pull/12051) |													
| Apache        | Flink | 1.13.0 | Workaround | |[source](https://flink.apache.org/2021/12/10/log4j-cve.html) |
| Apache        | Log4j | < 2.15.0 | Fix | |[source](https://logging.apache.org/log4j/2.x/security.html) |
| Apache        | Kafka | Unknown | Workaround/Vulnerable | Only vulnerable in certain configuration |[source](https://lists.apache.org/thread/lgbtvvmy68p0059yoyn9qxzosdmx4jdv) |
| Apache        | SOLR | 7.4.0 to 7.7.3, 8.0.0 to 8.11.0 | Fix | Versions before 7.4 also vulnerable when using several configurations |[source](https://solr.apache.org/security.html#apache-solr-affected-by-apache-log4j-cve-2021-44228) |
| Apero         | CAS | 6.3.x & 6.4.x | Fix | Other versions still in active maintainance might need manual inspection |[source](https://https://apereo.github.io/2021/12/11/log4j-vuln/) |
| Aptible       | Aptible | ElasticSearch 5.x | Fix | | [source](https://status.aptible.com/incidents/gk1rh440h36s?u=zfbcrbt2lkv4) |
| Atlassian     | Jira Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Confluence Server & Data Center| On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Bamboo Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Crowd Server & Data Center | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Fisheye | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Atlassian     | Crucible | On prem | Vulnerable | Only vulnerable when using non-default config, cloud version still under investigation |[source](https://confluence.atlassian.com/kb/faq-for-cve-2021-44228-1103069406.html) |
| Amazon        | EC2 |Amazon Linux 1 & 2 | Vulnerable | Default packages not vulnerable |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | OpenSearch | Unknown | Fix | |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | AWS Lambda | Unknown | Fix | Vulnerable when using aws-lambda-java-log4j2 |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Amazon        | AWS CloudHSM | < 3.4.1. | Fix | |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Azure         | Data lake store java | < 2.3.10 | Fix | |[source](https://github.com/Azure/azure-data-lake-store-java/blob/ed5d6304783286c3cfff0a1dee457a922e23ad48/CHANGES.md#version-2310) |


### B

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| Bitnami       | Unknown | Unknown | Fix | |[source](https://docs.bitnami.com/general/security/security-2021-12-10/) |
| Broadcom      | CA Advanced Protection | 9.1 & 9.1.01 | Workaround | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection Manager (SEPM) | 14.3 | Workaround | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Advanced Secure Gateway (ASG) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | BCAAA | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Content Analysis (CA)(SEPM) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Protection (CWP) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Cloud Workload Protection for Storage (CWP:S) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Critical System Protection (CSP) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Email Security Service (ESS) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | HSM Agent | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Industrial Control System Protection (ICSP) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Integrated Cyber Defense Manager (ICDm) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Integrated Secure Gateway (ISG) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Layer7 API Developer Portal | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Management Center (MC) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | PacketShaper (PS) S-Series | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | PolicyCenter (PC) S-Series | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Access Manager | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Access Manager Server Control | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Privileged Identity Manager | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Reporter | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Secure Access Cloud (SAC) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | SiteMinder (CA Single Sign-On) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | SSL Visibility (SSLV)| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Detection and Response (EDR) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Encryption (SEE) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection (SEP)| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Endpoint Protection (SEP) for Mobile| Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Mail Security for Microsoft Exchange (SMSMSE) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Messaging Gateway (SMG) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Protection Engine (SPE) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Symantec Protection for SharePoint Servers (SPSS) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | VIP Authentication Hub | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Web Isolation (WI) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | Web Security Service (WSS)) | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | WebPulse | Unknown | Investigation | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
| Broadcom      | CloudSOC Cloud Access Security Broker (CASB) | Unknown | Not vuln | |[source](https://support.broadcom.com/security-advisory/content/security-advisories/Symantec-Security-Advisory-for-Log4j-2-CVE-2021-44228-Vulnerability/SYMSA19793) |
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

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| Carbon Black | Cloud Workload Appliance | Unknown | Mitigation | More information on pages linked bottom of blogpost (behind login)| [source](https://community.carbonblack.com/t5/Documentation-Downloads/Log4Shell-Log4j-Remote-Code-Execution-CVE-2021-44228/ta-p/109134) |
| Carbon Black | EDR Servers| Unknown | Mitigation | More information on pages linked bottom of blogpost (behind login)| [source](https://community.carbonblack.com/t5/Documentation-Downloads/Log4Shell-Log4j-Remote-Code-Execution-CVE-2021-44228/ta-p/109134) |
| Cerberus | FTP | Unknown | Not vuln | |[source](https://support.cerberusftp.com/hc/en-us/articles/4412448183571-Cerberus-is-not-affected-by-CVE-2021-44228-log4j-0-day-vulnerability) |
| Checkpoint| Quantum Security Gateway | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| Quantum Security Management | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| CloudGuard | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| Infinity Portal | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| Harmony Endpoint & Harmony Mobile | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| SMB | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
| Checkpoint| ThreatCloud | Unknown | Not vuln | |[source](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk176865&partition=General&product=IPS) |
|Cisco|Cisco SocialMiner|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Extensible Network Controller (XNC)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Data Broker|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Insights|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Wide Area Application Services (WAAS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco AMP Virtual Private Cloud Appliance|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Adaptive Security Appliance (ASA) Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Advanced Web Security Reporting Application|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Content Security Management Appliance (SMA)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Email Security Appliance (ESA)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower 4100 Series|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower 9300 Security Appliances|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower Management Center|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Firepower Threat Defense (FTD)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Identity Services Engine (ISE)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Web Security Appliance (WSA)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ACI Multi-Site Orchestrator|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Application Policy Infrastructure Controller (APIC)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco CloudCenter Suite Admin|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco CloudCenter Workload Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Connected Grid Device Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Connected Mobile Experiences|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Crosswork Change Automation|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco DNA Assurance|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Data Center Network Manager (DCNM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Elastic Services Controller (ESC)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IoT Field Network Director (formerly Cisco Connected Grid Network Management System)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Modeling Labs|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Planner|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Services Orchestrator (NSO)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus Dashboard (formerly Cisco Application Services Engine)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Optical Network Planner|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Policy Suite|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Central for Service Providers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Assurance|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Collaboration Provisioning|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Infrastructure|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime License Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Network|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Optical for Service Providers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Provisioning|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Prime Service Catalog|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco UCS Performance Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Virtual Topology System - Virtual Topology Controller (VTC) VM|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco WAN Automation Engine (WAE)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ACI Virtual Edge|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco ASR 5000 Series Routers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco DNA Center|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Enterprise NFV Infrastructure Software (NFVIS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco GGSN Gateway GPRS Support Node|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IOS and IOS XE Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IOx Fog Director|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco IP Services Gateway (IPSG)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco MDS 9000 Series Multilayer Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco MME Mobility Management Entity|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Mobility Unified Reporting and Analytics System|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Assurance Engine|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Network Convergence System 2000 Series|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 5500 Platform Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 5600 Platform Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 6000 Series Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 7000 Series Switches|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Nexus 9000 Series Fabric Switches in Application Centric Infrastructure (ACI) mode|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco PDSN/HA Packet Data Serving Node and Home Agent|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco PGW Packet Data Network Gateway|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 1000 Series Routers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 2000 Series Routers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge 5000 Series Routers|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vEdge Cloud Router Platform|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco SD-WAN vManage|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Secure Network Analytics (SNA), formerly Stealthwatch|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco System Architecture Evolution Gateway (SAEGW)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco HyperFlex System|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco UCS Manager|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco BroadWorks|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Broadcloud Calling|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Computer Telephony Integration Object Server (CTIOS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Contact Center Domain Manager (CCDM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Contact Center Management Portal (CCMP)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Emergency Responder|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
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
|Cisco|Cisco Unified Customer Voice Portal|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified Intelligent Contact Management Enterprise|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Unified SIP Proxy Software|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Virtualized Voice Browser|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Exony Virtualized Interaction Manager (VIM)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Expressway Series|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Meeting Server|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco TelePresence Management Suite|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco TelePresence Video Communication Server (VCS)|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
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
|Cisco|AppDynamics: Refer to https://docs.appdynamics.com/display/PAA/Security+Advisory%3A+Apache+Log4j+Vulnerability|Unknown|Investigation||[source](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd)|
|Cisco|Cisco Webex Meetings Server| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Evolved Programmable Network Manager| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Integrated Management Controller (IMC) Supervisor| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Intersight Virtual Appliance| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco UCS Director| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Unified Contact Center Enterprise - Live Data server| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Video Surveillance Operations Manager| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Unified Communications Manager Cloud| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Webex Cloud-Connected UC (CCUC)| Unknown | Vulnerable | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Duo| Unknown | Fix | https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd
|Cisco|Cisco Jabber Guest|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Cloud Services Platform 2100|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Cloud Services Platform 5000 Series|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Tetration Analytics|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Adaptive Security Device Manager|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Registered Envelope Service|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Business Process Automation|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco CloudCenter Action Orchestrator|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Container Platform|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime Access Registrar|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime Cable Provisioning|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime Collaboration Deployment|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime IP Express|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime Network Registrar|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Prime Performance Manager|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Security Manager|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco UCS Central Software|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco IOS XR Software|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Nexus 3000 Series Switches|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Nexus 9000 Series Switches in standalone NX-OS mode|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco UCS C-Series Rack Servers - Integrated Management Controller|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Hosted Collaboration Mediation Fulfillment|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unified Communications Domain Manager|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unified Communications Manager / Cisco Unified Communications Manager Session Management Edition|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unified Communications Manager IM & Presence Service (formerly CUPS)|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unified Intelligence Center|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unity Connection|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Unity Express|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
|Cisco|Cisco Smart Software Manager On-Prem|Unknown|Not vuln||https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd|
| Citrix       | NetScaler ADC | Unknown | Investigation |  Implementation not using WlonNS feature, is not impacted | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | NetScaler Gateway | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Analytics | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Application Delivery Management (NetScaler MAS)  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Hypervisor (XenServer)   | Unknown | Not Vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | SD-WAN  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Virtual Apps and Desktops (XenApp & XenDesktop)    | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Workspace  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) | 
| Citrix       | Workspace App  | Unknown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Sharefile  | Unknown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |
| Cloudflare | Cloudflare WAF | Unknown | Mitigation | | [source](https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/) |
| cPanel | cPanel | Unknown | Mitigation | | [source](https://forums.cpanel.net/threads/log4j-cve-2021-44228-does-it-affect-cpanel.696249/) |
| Commvault | All products | Unknown | Not vuln | [source](https://community.commvault.com/technical-q-a-2/log4j-been-used-in-commvault-1985?postid=11745#post11745) |
| Connect2id | Connect2id server | < 12.5.1 | Fix | [source](https://connect2id.com/blog/connect2id-server-12-5-1) |
| Connectwise | Perch | Unknown | Fix || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Manage on-premise's Global Search  | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Marketplace | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | Global search capability of Manage Cloud | Unknown | Mitigation || [source](https://www.connectwise.com/company/trust/advisories) |
| Connectwise | StratoZen | Unknown | Mitigation | Urgent action for self-hosted versions |[source](https://www.connectwise.com/company/trust/advisories) |
| Contrast | Hosted SaaS Enviroments | All | Fix | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | On-premises (EOP) Environments | All | Fix/Mitigation | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | Java Agent | All | Not vuln | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Contrast | Scan | All | Fix | |[source](https://support.contrastsecurity.com/hc/en-us/articles/4412612486548) |
| Coralogix | Coralogix | Unknown | Fix | |[source](https://status.coralogix.com/incidents/zzfn8t0fzdy2?u=1q9952ycm1gr) |
| Couchbase | Couchbase ElasticSearch connector| < 4.3.3 & 4.2.13 | Fix | |[source](https://forums.couchbase.com/t/ann-elasticsearch-connector-4-3-3-4-2-13-fixes-log4j-vulnerability/32402) |
| Cybereason | All Cybereason products | Unknown | Not vuln | |[source](https://www.cybereason.com/blog/cybereason-solutions-are-not-impacted-by-apache-log4j-vulnerability-cve-2021-44228) |

### D
| Datto | All Datto products | Unknown | Not vuln | |[source](https://www.datto.com/blog/dattos-response-to-log4shell) |
| Debian | Apache-log4j.1.2 | Stretch, buster, bookworm | Fix | |[source](https://security-tracker.debian.org/tracker/CVE-2021-44228) |
| Debian | Apache-log4j2 | Stretch(security), buster(security), bullseye(security), bookworm, sid | Fix/Vulnerable | No fix yet for stretch, buster and bookworm |[source](https://security-tracker.debian.org/tracker/CVE-2021-44228) |
| Dell | All products | Unknown | Investigation | Dell is still investigating, new advisories will be published at https://www.dell.com/support/security/nl-nl |[source](https://www.dell.com/support/kbdoc/nl-nl/000194372/dsn-2021-007-dell-response-to-apache-log4j-remote-code-execution-vulnerability) |
| Docker | Docker infrastructure | Unknown | Not vuln | Docker infrastructure not vulnerable, Docker images could be vulnerable. For more info see source. |[source](https://www.docker.com/blog/apache-log4j-2-cve-2021-44228/) |
| Dropwizard | Dropwizard | Unknown | Not vuln | Only vulnerable if you manually added Log4j |[source](https://twitter.com/dropwizardio/status/1469285337524580359) |
| Dynatrace | Dynatrace Cloud Services | Unknown | Fix | | [source](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/Impact-of-log4j-zero-day-vulnerability/m-p/177259/highlight/true#M19282) |
| Dynatrace | ActiveGates | 1.229.49.20211210-165018, 1.227.31.20211210-164955, 1.225.29.20211210-164930, 1.223.30.20211210-164926 | Fix | |[source](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/Impact-of-log4j-zero-day-vulnerability/m-p/177259/highlight/true#M19282) |

### E

### F

### G

### H 

### I

### J

### K

### L

### M

### N

### O

### P

### Q
| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| QlikTech International | Compose | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Nprinting | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | QEM products | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Qlik Replicate | | Investigation | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | Qlik Sense Enterprise | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QlikTech International | QlikView | | Not Vuln | | [source](https://community.qlik.com/t5/Support-Updates-Blog/Vulnerability-Testing-Apache-Log4j-reference-CVE-2021-44228-also/ba-p/1869368) |
| QOS.ch          | SLF4J Simple Logging Facade for Java | |  | SLF4J API doesn't protect against the vulnerability when using a vulnerable version of log4j | [source](http://slf4j.org/log4shell.html) |

### R
| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| Red Hat         | Red Hat OpenShift Container Platform 4	openshift4/ose-metering-presto |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 4	openshift4/ose-metering-hive |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 4	openshift4/ose-logging-elasticsearch6 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Container Platform 3.11	openshift3/ose-logging-elasticsearch5 |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenStack Platform 13 (Queens)	opendaylight |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
| Red Hat         | Red Hat OpenShift Logging	logging-elasticsearch6-container |  | Vulnerable | | [source](https://access.redhat.com/security/cve/cve-2021-44228) |
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
| RSA             | SecurID Authentication Manager |  | Not Vuln | Version 8.6 Patch 1 contains a version of log4j that is vulnerable, but this vulnerability is not exploitable. | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Authentication Manager Prime |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Authentication Manager WebTier |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Identity Router (On-Prem component of Cloud Authentication Service) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Governance and Lifecycle (SecurID G&L) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |
| RSA             | SecurID Governance and Lifecycle Cloud (SecurID G&L Cloud) |  | Not Vuln | | [source](https://community.rsa.com/t5/general-security-advisories-and/rsa-customer-advisory-apache-vulnerability-log4j2-cve-2021-44228/ta-p/660501) |


### S
| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| SonicWall       | Gen5 Firewalls (EOS) |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Gen6 Firewalls |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Gen7 Firewalls |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SonicWall Switch |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SMA 100 |  | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | SMA 1000 | 12.1.0, 12.4.1 | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
| SonicWall       | Email Security | 10.x | Not Vuln | | [source](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0032) |
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

### T

### U 

### V

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| VMware       |  Horizon | 8.x, 7.x | Workaround |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87073) |
| VMware       | vCenter Server  | 7.x, 6.x | Workaround |  Running on: Virtual Appliance | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87081?lang=en_US) |
| VMware       | vCenter Server  | 6.x | Vulnable |  Running on: Windows | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | HCX | 4.x, 3.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/86169) |
| VMware       | NSX-T Data Center  | 3.x, 2.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87086) |
| VMware       | Unified Access Gateway  | 21.x, 20.x, 3.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87092) |
| VMware       | Workspace ONE Access   | 21.x, 20.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87090) |
| VMware       | Identity Manager    | 3.3.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87093) |
| VMware       | vRealize Operations    | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87076) |
| VMware       | vRealize Operations Cloud Proxy     | Any | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87080) |
| VMware       | vRealize Log Insight     | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://kb.vmware.com/s/article/87089) |
| VMware       | vRealize Automation     | 8.x, 7.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | vRealize Lifecycle Manager  | 8.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | vSphere ESXi | Unknown | Not Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Telco Cloud Automation | 2.x, 1.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | Carbon Black Cloud Workload Appliance | 1.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-Cloud/ta-p/109167) |
| VMware       | Carbon Black EDR Server  | 7.x, 6.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-EDR/ta-p/109168) |
| VMware       | Site Recovery Manager   | 8.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | Tanzu GemFire   | 8.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-all-GemFire-versions?language=en_US)|
| VMware       | Tanzu Greenplum  | 6.x | Workaround |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [Workaround](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-All-Greenplum-Versions?language=en_US)|
| VMware       | Tanzu Operations Manager  | 2.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [Workaround](https://community.pivotal.io/s/article/5004y00001mPn2N1639255611105?language=en_US) |
| VMware       | Tanzu Application Service for VMs  | 2.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [Workaround](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US) |
| VMware       | Tanzu Kubernetes Grid Integrated Edition   | 2.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [Workaround](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US) |
| VMware       | Tanzu Observability by Wavefront Nozzle   | 3.0.3 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/wavefront-nozzle) |
| VMware       | Healthwatch for Tanzu Application Service  | 2.1.7, 1.8.6 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/p-healthwatch) |
| VMware       | Cloud Services for VMware Tanzu  | 3.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Cloud Gateway for VMware Tanzu  | 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Spring Cloud Gateway for Kubernetes  | 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | API Portal for VMware Tanzu  | 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Single Sign-On for VMware Tanzu Application Service  | 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | App Metrics  | 2.1.1 | Fix |   | [source](https://kb.vmware.com/s/article/87068), [fix](https://network.pivotal.io/products/apm) |
| VMware       | VMware vCenter Cloud Gateway  | 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068)|
| VMware       | VMware Tanzu SQL with MySQL for VMs  | 2.x, 1.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068)|
| VMware       | VMware vRealize Orchestrator   | 8.x, 7.x | Vuln |   | [source](https://kb.vmware.com/s/article/87068)|
| VMware       | VMware Cloud Foundation  | 4.x, 3.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [Workaround](https://kb.vmware.com/s/article/87095)|
| VMware       | VMware Workspace ONE Access Connector (VMware Identity Manager Connector)  | 19.03.0.1, 20.x, 21.x | Workaround |   | [source](https://kb.vmware.com/s/article/87068), [Workaround](https://kb.vmware.com/s/article/87091)|



### W

### X

### Y

### Z





