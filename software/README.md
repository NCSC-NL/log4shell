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
| Amazon        | AWS CloudHSM | <3.4.1. | Fix | |[source](https://aws.amazon.com/security/security-bulletins/AWS-2021-005/) |
| Azure         | Data lake store java | <2.3.10 | Fix | |[source](https://github.com/Azure/azure-data-lake-store-java/blob/ed5d6304783286c3cfff0a1dee457a922e23ad48/CHANGES.md#version-2310) |


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
| Citrix       | NetScaler ADC | Unknown | Investigation |  Implementation who are not using WlonNS feature, are not impacted | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | NetScaler Gateway | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Analytics | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Application Delivery Management (NetScaler MAS)  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Hypervisor (XenServer)   | Unknown | Not Vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | SD-WAN  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Virtual Apps and Desktops (XenApp & XenDesktop)    | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Workspace  | Unknown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) | 
| Citrix       | Workspace App  | Unknown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Sharefile  | Unknown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |

### D

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





