# List of software (un)affected by the log4shell CVEs
[About this list](README.md)

[0-9](software_list_0-9.md) [A](software_list_a.md) [B](software_list_b.md) [C](software_list_c.md) [D](software_list_d.md) [E](software_list_e.md) [F](software_list_f.md) [G](software_list_g.md) [H](software_list_h.md) [I](software_list_i.md) [J](software_list_j.md) [K](software_list_k.md) [L](software_list_l.md) [M](software_list_m.md) [N](software_list_n.md) [O](software_list_o.md) [P](software_list_p.md) [Q](software_list_q.md) [R](software_list_r.md) [S](software_list_s.md) [T](software_list_t.md) [U](software_list_u.md) [V](software_list_v.md) [W](software_list_w.md) [X](software_list_x.md) [Y](software_list_y.md) [Z](software_list_z.md)

### N

| Supplier | Product | Version (see Status) | Status CVE-2021-4104 | Status CVE-2021-44228 | Status CVE-2021-45046 | Status CVE-2021-45105 | Notes | Links |
|:---------|:--------|:--------------------:|:--------------------:|:---------------------:|:---------------------:|:---------------------:|:------|------:|
|National Instruments|OptimalPlus|Vertica, Cloudera, Logstash| |Vulnerable| | |(Limited to deployments running Vertica, Cloudera, or Logstash) Contact Technical Support|[link](https://www.ni.com/en-us/support/documentation/supplemental/21/ni-response-to-apache-log4j-vulnerability-.html)|
|N-able|Backup| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|Mail Assure| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|MSP Manager| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|N-central| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|Passportal| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|Risk Intelligence| | |Vulnerable| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|RMM| |Not vuln|Fix| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|N-able|Take Control| | |Not vuln| | ||[source](https://www.n-able.com/security-and-privacy/apache-log4j-vulnerability)|
|Nagios|Core| | |Not vuln| | ||[source](https://www.nagios.com/news/2021/12/update-on-apache-log4j-vulnerability/)|
|Nagios|Log Server| | |Not vuln| | ||[source](https://www.nagios.com/news/2021/12/update-on-apache-log4j-vulnerability/)|
|Nagios|XI| | |Not vuln| | ||[source](https://www.nagios.com/news/2021/12/update-on-apache-log4j-vulnerability/)|
|Nakivo|Backup & Replication| |Not vuln|Workaround| | |manual fix by removing JndiLookup.class located in libs\log4j-core-2.2.jar.  https://forum.nakivo.com/index.php?/topic/7574-log4j-cve-2021-44228/#comment-9145|[source](/NCSC-NL/log4shell/blob/main/NCSC-NL/log4shell/blob/main/software/vendor-statements/nakivo_email.png)|
|Nelson|All|0.16.185| |Vulnerable| | |Workaround is available, but not released yet.|[source](https://github.com/getnelson/nelson/blob/f4d3dd1f1d4f8dfef02487f67aefb9c60ab48bf5/project/custom.scala)|
|Neo4j|All|>=4.2.12, >=4.3.8, >=4.4.1|Not vuln|Fix| | ||[source](https://community.neo4j.com/t/log4j-cve-mitigation-for-neo4j/48856) [source_fix](https://neo4j.com/security/log4j/?_gl=1*21owwo*_ga*MjE0NzMyNTYxMy4xNjM4MTE2NTM0*_ga_DL38Q8KGQC*MTYzOTY1NTgyMS4yNS4wLjE2Mzk2NTU4MjEuMA..&_ga=2.221851932.50302124.1639655825-2147325613.1638116534)|
|Neo4j|Graph Database|Version >4.2, <4..2.12| |Vulnerable| | |||
|NetApp|Brocade SAN Naviator| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Cloud Insights Acquisition Unit| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Cloud Manager| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Cloud Secure| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Element Plug-in for vCenter Server| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|HCI Compute Node| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Management Services for Element Software and NetApp HCI| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|Multiple NetApp products| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|OnCommand Insight| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|ONTAP Tools for VMware vSphere| | |Vulnerable| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|SnapCenter Plug-in for VMware vSphere| |Not vuln|Workaround| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/#:~:text=Workarounds-,snapleft%20plug-in%20for%20vmware%20vsphere)|
|NetApp|SolidFire & HCI Management Node| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|SolidFire Plug-in for vRealize Orchestrator (SolidFire vRO)| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|SolidFire, Enterprise SDS & HCI Storage| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetApp|SolidFireStorage Replication Adapter| | |Not vuln| | ||[source](https://security.netapp.com/advisory/ntap-20211210-0007/)|
|NetCore|Unimus|2.1.4|Not vuln|Fix| | ||[source](https://download.unimus.net/unimus/Changelog.txt)|
|Netcup|All| | | | | ||[Netcup Statement](https://www.netcup-news.de/2021/12/14/pruefung-log4j-sicherheitsluecken-abgeschlossen/)|
|Netflix|atlas|1.6.6|Not vuln|Workaround| | ||[source](https://github.com/Netflix/atlas/commit/5baff2b656a45886b85968a4b66f33bd36c648be)|
|Netflix|dgs-framework|< 4.9.11|Not vuln|Fix| | ||[source](https://github.com/Netflix/dgs-framework/releases/tag/v4.9.11)|
|Netflix|spectator|< 1.0.9|Not vuln|Fix| | ||[source](https://github.com/Netflix/spectator/releases/tag/v1.0.9)|
|Netflix|zuul| |Not vuln|Workaround| | ||[source](https://github.com/Netflix/zuul/commit/280f20cd51deb7e72275625d5ec556aae06f6a29)|
|Netgate|pfSense|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://forum.netgate.com/topic/168417/java-log4j-vulnerability-is-pfsense-affected)|
|NetGate PFSense|All| | | | | ||[NetGate PFSense Forum](https://forum.netgate.com/topic/168417/java-log4j-vulnerability-is-pfsense-affected/35)|
|Netgear|All| |Not vuln|Not vuln|Not vuln|Not vuln||[source](https://community.netgear.com/t5/Smart-Plus-and-Smart-Pro-Managed/Has-Netgear-GS748TS-been-affected-by-Log4J/m-p/2173582#M19998)|
|NetIQ|Access Manager|>= 4.5.x & >= 5.0.x|Not vuln|Workaround| | ||[source](https://portal.microfocus.com/s/article/KM000002997)|
|NetIQ|Advanced Authentication|>= 6.x|Not vuln|Workaround| | ||[source](https://portal.microfocus.com/s/article/KM000003047)|
|NetIQ|eDirectory|>= 9.2.x|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://portal.microfocus.com/s/article/KM000003035)|
|NetIQ|Identity Manager|>= 4.7.x & >= 4.8.x|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://portal.microfocus.com/s/article/KM000003035)|
|NetIQ|iManager|>= 3.2.x|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://portal.microfocus.com/s/article/KM000003035)|
|Netwrix|Auditor| |Not vuln|Not vuln|Not vuln|Not vuln||[source](http://www.publicnow.com/view/EA90CB461F5F0A1BA339E2AC55C719CA5AD58CE4)|
|New Relic|Containerized Private Minion (CPM)|3.0.55|Not vuln|Fix| | ||[source](https://docs.newrelic.com/docs/security/new-relic-security/security-bulletins/security-bulletin-nr21-04/)|
|New Relic|Java Agent|6.5.1 & 7.4.1|Not vuln|Fix| | ||[source](https://docs.newrelic.com/docs/security/new-relic-security/security-bulletins/security-bulletin-nr21-03/)|
|NextCloud|All| |Not vuln|Not vuln|Not vuln|Not vuln|Invidivual plugins not developed as part of Nextcloud core may be vulnerable.|[source](https://help.nextcloud.com/t/apache-log4j-does-not-affect-nextcloud/129244)|
|Nextflow|All|21.04.0.5552|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://www.nextflow.io/docs/latest/index.html)|
|NextGen Healthcare|Mirth| | |Not vuln| | ||[source](https://github.com/nextgenhealthcare/connect/discussions/4892#discussioncomment-1789526)|
|Nexus Group|All| | | | | ||[Nexus Group Docs](https://doc.nexusgroup.com/pages/viewpage.action?pageId=83133294)|
|NI (National Instruments)|All| | | | | ||[NI Support Link](https://www.ni.com/en-us/support/documentation/supplemental/21/ni-response-to-apache-log4j-vulnerability-.html)|
|Nice Software (AWS) EnginFRAME|All| | | | | ||[Nice Software EnginFRAME Link](https://download.enginframe.com/)|
|NiceLabel|All| |Not vuln|Not vuln|Not vuln|Not vuln||[source](https://help.nicelabel.com/hc/en-001/articles/4413846986385-Apache-Log4j-Vulnerability-Log4Shell-CVE-2021-44228-does-not-affect-NiceLabel-applications)|
|NinjaRMM|All| | | | | |This advisory is available to customers only and has not been reviewed by CISA|[NinjaRMM Article](https://ninjarmm.zendesk.com/hc/en-us/articles/4416226194189-12-10-21-Security-Declaration-NinjaOne-not-affected-by-CVE-2021-44228-log4j-)|
|Nomachine|All|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://forums.nomachine.com/topic/apache-log4j-notification)|
|NoviFlow|All| | | | | ||[Noviflow Link](https://noviflow.com/noviflow-products-and-the-log4shell-exploit-cve-2021-44228/)|
|NSA|Ghidra|< 10.1|Not vuln|Fix| | ||[source](https://github.com/NationalSecurityAgency/ghidra/blob/2c73c72f0ba2720c6627be4005a721a5ebd64b46/README.md#warning) [fix](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_10.1_build)|
|Nulab|Backlog|N/A (SaaS)|Not vuln|Fix|Fix|Fix||[source](https://nulab.com/blog/company-news/log4shell/)|
|Nulab|Backlog Enterprise (On-premises)|1.11.7|Not vuln|Fix|Fix|Fix||[source](https://nulab.com/blog/company-news/log4shell/)|
|Nulab|Cacoo|N/A (SaaS)|Not vuln|Fix|Fix|Fix||[source](https://nulab.com/blog/company-news/log4shell/)|
|Nulab|Cacoo Enterprise (On-premises)|4.0.4|Not vuln|Fix|Fix|Fix||[source](https://nulab.com/blog/company-news/log4shell/)|
|Nulab|Typetalk|N/A (SaaS)|Not vuln|Fix|Fix|Fix||[source](https://nulab.com/blog/company-news/log4shell/)|
|Nutanix|AHV|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|AOS|LTS (including Prism Element), Community Edition|Not vuln|Not vuln|Not vuln|Not vuln||[Nutanix Security Advisory](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|AOS|STS (including Prism Element)|Not vuln|Fix| | |Patched in 6.0.2.4, available on the Portal for|[Nutanix Security Advisory](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|AOS (Community Edition)|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|AOS (LTS)|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|AOS (STS)|All|Not vuln|Workaround|Workaround|Vulnerable|Non exploitable dormant code present, Patch 6.0.2.4 will remove dormant code|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Beam|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|BeamGov|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Calm|All|Not vuln|Not vuln|Not vuln|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Calm|SaaS|Not vuln|Vulnerable|Vulnerable|Vulnerable|WAF updated to block exploit, backend patch pending|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Calm Tunnel VM|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Collector|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Collector Portal|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Data Lens|SaaS|Not vuln|Not vuln|Not vuln|Not vuln|WAF updated to block exploit|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Era|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|File Analytics|2.1.x, 2.2.x, 3.0+| |Vulnerable| | |Mitigated in version 3.0.1 which is available on the Portal for download. Mitigation is available  https://portal.nutanix.com/kb/12499 here|[Nutanix Security Advisory](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Files|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Flow|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Flow Security Cental| |Not vuln|Fix| | |Saas-Based Procuct.  See Advisory.|[Nutanix Security Advisory](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Flow Security Central|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Foundation|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Frame|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|FrameGov|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|FSCVM|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|General Guidance| | | | | |Nutanix updating Security Advisory #23 multiple times per day, please check source link for absolute latest status|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Insights|SaaS|Not vuln|Not vuln|Not vuln|Not vuln|WAF updated to block exploit|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Karbon|All|Not vuln|Workaround|Workaround|Vulnerable||[source](https://portal.nutanix.com/kb/12483)|
|Nutanix|Karbon Platform Service|SaaS|Not vuln|Vulnerable|Vulnerable|Vulnerable|WAF updated to block exploit, Patch is verifying|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|LCM|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Leap|SaaS|Not vuln|Vulnerable|Vulnerable|Vulnerable|WAF updated to block exploit, Patch is pending|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Mine|All|Not vuln|Workaround|Workaround|Vulnerable||[source](https://portal.nutanix.com/kb/12484)|
|Nutanix|Move|All|Not vuln|Not vuln|Not vuln|Not vuln|https://download.nutanix.com/alerts/Security_Advisory_0023.pdf||
|Nutanix|MSP|All|Not vuln|Workaround|Workaround|Vulnerable||[source](https://portal.nutanix.com/kb/12482)|
|Nutanix|NCC|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|NGT|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Objects|All|Not vuln|Workaround|Workaround|Vulnerable||[source](https://portal.nutanix.com/kb/12482)|
|Nutanix|Prism Central|All|Not vuln|Vulnerable|Vulnerable|Vulnerable|Release pending|[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Sizer|SaaS|Not vuln|Fix|Fix|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Volumes|All|Not vuln|Not vuln|Not vuln|Vulnerable||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|Nutanix|Witness VM|All|Not vuln|Workaround|Workaround|Vulnerable||[source](https://portal.nutanix.com/kb/12491)|
|Nutanix|X-Ray|All|Not vuln|Not vuln|Not vuln|Not vuln||[source](https://download.nutanix.com/alerts/Security_Advisory_0023.pdf)|
|NVIDIA|CUDA Toolkit Nsight Eclipse Edition|11.0|Not vuln|Fix|Fix| ||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|CUDA Toolkit Visual Profiler|11.5 and Prior| |Vulnerable|Vulnerable| |Updated CUDA Toolkit version available mid-January 2022|[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|DGX systems|DGX OS 4 and DGX OS 5|Not vuln|Fix|Fix|Fix|Updates can be installed through the package manager|[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|GeForce Experience client software| | |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|GeForceNOW client software| | |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|GPU Display Drivers for Windows and Linux| | |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|L4T Jetson Products| | |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|NetQ|4.1.0| |Fix|Fix|Fix||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|Networking products|All (except for NetQ)| |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|Broadcast|All| |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|Maxine|All| |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|SHIELD TV| | |Not vuln|Not vuln|Not vuln||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NVIDIA|vGPU software license server|2021.7 and 2020.5 Update 1| |Workaround|Workaround|Workaround||[source](https://nvidia.custhelp.com/app/answers/detail/a_id/5294)|
|NXLog|Manager|5.x| |Not vuln| | ||[source](https://nxlog.co/news/apache-log4j-vulnerability-cve-2021-44228)|
