# Overview of software (un)affected by Log4j

This directory contains [an overview of software (un)affected by the Log4shell vulnerabilities](software_list.md). NCSC-NL and partners are attempting to maintain a list of all known vulnerable and not vulnerable software. Listed software is paired with specific information regarding which version contains the security fixes and which software still requires fixes. Please note that this vulnerability may also occur in custom software developed within your organisation. These occurrences are not registered in this overview.

NCSC-NL has concluded that the new vulnerability (CVE-2021-44832) has a low chance of being exploited and will therefore exclude this vulnerability from this GitHub.

#### NCSC Advisories
NCSC-NL has published a HIGH/HIGH advisory for the Log4j vulnerability. Normally we would update the HIGH/HIGH advisory for vulnerable software packages, however due to the extensive amounts of expected updates we have created a list of known vulnerable software in the software directory.

#### Daily CSV/JSON releases
Daily releases of this software list are listed, including CSV and JSON files, in the [releases](https://github.com/NCSC-NL/log4shell/releases) overview. Please check the [software list parser](https://github.com/NCSC-NL/log4shell/tree/main/tools/log4shell_softwarelist) tool to generate a CSV or JSON on your own.

> **Disclaimer:** _We aim to provide as the information as accurately as possible with the resources available to us. However, we do not have the capacity to monitor all software for updates/fixes. You are advised to review the links provided for available updates. If you find updates or mistakes, please contribute by creating a Pull Request. [Learn how](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository).

## Software overview
The following status labels are in use:

| Status CVE-2021-xxx | Description                                                      |
|:--------------------|:-----------------------------------------------------------------|
| Vulnerable          | Software is vulnerable to CVE-2021-xxx.                          |
| Fix                 | Software contains a fix for CVE-2021-xxx.                        |
| Workaround          | Software is vulnerable but mitigation steps are available.       |
| Not vuln            | Software is **NOT** vulnerable for CVE-2021-xxx.                 |
| Investigation       | Software is under investigation whether it is vulnerable or not. |

The `Version` relates to the `Status` column. If `Status` field is set to 'Vulnerable', the `Version` field indicates vulnerable version(s) if these version numbers are known to us. If `Status` is set to 'Fix', the `Version` field indicates the version(s) in which the fix was introduced. Some products do not have clear version numbers, in which case the `Version` field is empty. We advise readers to follow the provided source links for more detailed information.

[0-9](software_list_0-9.md) [A](software_list_a.md) [B](software_list_b.md) [C](software_list_c.md) [D](software_list_d.md) [E](software_list_e.md) [F](software_list_f.md) [G](software_list_g.md) [H](software_list_h.md) [I](software_list_i.md) [J](software_list_j.md) [K](software_list_k.md) [L](software_list_l.md) [M](software_list_m.md) [N](software_list_n.md) [O](software_list_o.md) [P](software_list_p.md) [Q](software_list_q.md) [R](software_list_r.md) [S](software_list_s.md) [T](software_list_t.md) [U](software_list_u.md) [V](software_list_v.md) [W](software_list_w.md) [X](software_list_x.md) [Y](software_list_y.md) [Z](software_list_z.md)

