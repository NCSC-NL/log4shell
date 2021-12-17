# Log4j Microsoft Defender queries

### Find callback connections
Possible Malicious Indicators in Cloud Application Events. This query is designed to flag exploitation attempts for cases where the attacker is sending the crafted exploitation string using vectors such as User-Agent, Application or Account name. The hits returned from this query are most likely unsuccessful attempts, however the results can be useful to identity attackers’ details such as IP address, Payload string, Download URL, etc.

```plain
CloudAppEvents
| where Timestamp > datetime("2021-12-09")
| where UserAgent contains "jndi:" 
or AccountDisplayName contains "jndi:"
or Application contains "jndi:"
or AdditionalFields contains "jndi:"
| project ActionType, ActivityType, Application, AccountDisplayName, IPAddress, UserAgent, AdditionalFields
```

### Possible vulnerable applications via Threat and Vulnerability Management
This query looks for possibly vulnerable applications using the affected Log4j component. Triage the results to determine applications and programs that may need to be patched and updated.

```plain
DeviceTvmSoftwareInventory
| where SoftwareName contains "log4j"
| project DeviceName, SoftwareName, SoftwareVersion
```

## Find callback connections
[Microsoft's Azure Sentinel IoC List](https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Sample%20Data/Feeds/Log4j_IOC_List.csv)
