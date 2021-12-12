# Log4j overview related software

This page contains an overview of any related software regarding the Log4j vulnerability. On this page NCSC-NL will maintain a list of all known vulnerable and not vulnerable software. Futhermore any reference to the software will contain specific information regarding which version contains the security fixes, and which software still requires mitigation.

NCSC-NL will use the following status 

| Status         | Description                  |
|:---------------|:-----------------------------|
| Vulnerable     | Software is vulnerable for CVE-2021-44228. |
| Fix            | Software contains a fix for CVE-2021-44228 |
| Patch          | Software is vulnerable but mitigation steps are available |
| Not Vuln     | Software is **NOT** vulnerable for CVE-2021-44228. |
| Investigation     | Software is under investigation whether it is vulnerable or not |


## Software overview

### A

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
|                  									   ||||

### B

| Supplier        | Product         | Version         | Status          | Notes           |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|
|                  									   ||||

### C

| Supplier        | Product         | Version         | Status          | Notes           | Links |
|:----------------|:----------------|:---------------:|:---------------:|:----------------|-----------:|
| Citrix       | NetScalar ADC | Unkown | Investigation |  Implementation who are not using WlonNS feature, are not impacted | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | NetScalar Gateway | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Analytics | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Application Delivery Management (NetScaler MAS)  | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Hypervisor (XenServer)   | Unkown | Not Vuln |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | SD-WAN  | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Virtual Apps and Desktops (XenApp & XenDesktop)    | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Workspace  | Unkown | Investigation |  | [source](https://support.citrix.com/article/CTX335705) | 
| Citrix       | Workspace App  | Unkown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |
| Citrix       | Sharefile  | Unkown | Investigation|  | [source](https://support.citrix.com/article/CTX335705) |

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
| VMware       |  Horizon | 8.x, 7.x | Patch |   | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87073) |
| VMware       | vCenter Server  | 7.x, 6.x | Patch |  Running on: Virtual Appliance | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87081?lang=en_US) |
| VMware       | vCenter Server  | 6.x | Vulnable |  Running on: Windows | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | HCX | 4.x, 3.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/86169) |
| VMware       | NSX-T Data Center  | 3.x, 2.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87086) |
| VMware       | Unified Access Gateway  | 21.x, 20.x, 3.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87092) |
| VMware       | Workspace ONE Access   | 21.x, 20.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87090) |
| VMware       | Identity Manager    | 3.3.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87093) |
| VMware       | vRealize Operations    | 8.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87076) |
| VMware       | vRealize Operations Cloud Proxy     | Any | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87080) |
| VMware       | vRealize Log Insight     | 8.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://kb.vmware.com/s/article/87089) |
| VMware       | vRealize Automation     | 8.x, 7.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | vRealize Lifecycle Manager  | 8.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | vSphere ESXi | Unkown | Not Vuln |   | [source](https://kb.vmware.com/s/article/87068) |
| VMware       | Telco Cloud Automation | 2.x, 1.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | Carbon Black Cloud Workload Appliance | 1.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-Cloud/ta-p/109167) |
| VMware       | Carbon Black EDR Server  | 7.x, 6.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://community.carbonblack.com/t5/Threat-Research-Docs/Log4Shell-Mitigation-Steps-for-VMware-Carbon-Black-EDR/ta-p/109168) |
| VMware       | Site Recovery Manager   | 8.x | Vuln |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)|
| VMware       | Tanzu GemFire   | 8.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-all-GemFire-versions?language=en_US)|
| VMware       | Tanzu Greenplum  | 6.x | Patch |  | [source](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), [patch](https://community.pivotal.io/s/article/Workaround-to-address-CVE-2021-44228-Apache-Log4j-Remote-Code-Execution-for-All-Greenplum-Versions?language=en_US)|
| VMware       | Tanzu Operations Manager  | 2.x | Patch |   | [source](https://kb.vmware.com/s/article/87068), [patch](https://community.pivotal.io/s/article/5004y00001mPn2N1639255611105?language=en_US) |
| VMware       | Tanzu Application Service for VMs  | 2.x | Patch |   | [source](https://kb.vmware.com/s/article/87068), [patch](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US) |
| VMware       | Tanzu Kubernetes Grid Integrated Edition   | 2.x | Patch |   | [source](https://kb.vmware.com/s/article/87068), [patch](https://community.pivotal.io/s/article/Workaround-instructions-to-address-CVE-2021-44228-in-Tanzu-Application-Service-2-7-through-2-12?language=en_US) |
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
| VMware       | VMware Cloud Foundation  | 4.x, 3.x | Patch |   | [source](https://kb.vmware.com/s/article/87068), [patch](https://kb.vmware.com/s/article/87095)|
| VMware       | VMware Workspace ONE Access Connector (VMware Identity Manager Connector)  | 19.03.0.1, 20.x, 21.x | Patch |   | [source](https://kb.vmware.com/s/article/87068), [patch](https://kb.vmware.com/s/article/87091)|



### W

### X

### Y

### Z





