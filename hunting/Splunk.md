# Log4j Splunk queries

## Find used versions

### Stacktraces
Find the used version based on stacktraces.

```plain
index=* org.apache.logging.log4j 
| rex field=_raw "\[(?<log4j_version>log4j-[^]]+)" 
| where isnotnull(log4j_version) 
| stats latest(log4j_version) AS log4j_version, max(_time) AS lastTime, values(index) AS org_index, values(sourcetype) AS org_sourcetype by host 
| eval lastTime=strftime(lastTime,"%F %T")
| rex field=log4j_version "(?:log4j-)(?<component>[^-]+)-(?<version>\d+.\d+.\d+)"
| table lastTime host log4j_version component version org_index org_sourcetype
```

### Windows process creation
Find the used version based on the windows process creation events. 

**Note**: This requires a GPO change to enable the get the "Process Command Line" field filled out in your logs. See this [Microsoft site](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing) on how to do this.

```plain
index=[WINDOWS SECURITY INDEX] "EventCode=4688" log4j
| rex field="Process_Command_Line" max_match=0 "(?<log4j_version>log4j(?!\.configuration|\.properties).*?\.jar)" 
| mvexpand log4j_version
| rex field=log4j_version "(?:log4j.*?)(?:(?<component>-[^-]+)-|-)(?<version>\d+.\d+.\d+)"
| eval component=trim(component,"-")
| fillnull component value="unknown"
| stats values(log4j_version) AS log4j_version, values(component) AS component, values(version) AS version, max(_time) AS lastTime, values(index) AS org_index, values(sourcetype) AS org_sourcetype by host 
| where isnotnull(version)
| eval lastTime=strftime(lastTime,"%F %T")
| table lastTime host log4j_version component version org_index org_sourcetype
```

## Find callback connections
Find connections back to the JNDI domains

### IP based JNDI connections
Find connections in your firewall logs that try to make a connection to a IP address that was in the jndi string.

_The below query will first look in every non-internal index for the term jndi, it will than extract the destination domain and filter out the valid IP addresses.</ br>
It only looks for connections that where not blocked if you want everything remove the `action="blocked"` part._
```plain
index=[FIREWALL INDEX] action!="blocked"
    [| search index=* TERM(jndi) 
    | rex max_match=0 "(?i)jndi\:(?:[^\/]*)\/{1,2}(?<jndi_domain>[^\/\s\,]+)" 
    | stats c by jndi_domain 
    | eval jndi_domain=replace(lower(jndi_domain), ".*?\$\{[a-z0-9-_:\.]+?\}","*"), jndi_domain=trim(jndi_domain,"}"),
      ip_version=case(match(jndi_domain,"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"),"ipv6", match(jndi_domain,"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"),"ipv4", true(),"domain"), 
      ipv4=if(ip_version=="ipv4",jndi_domain,null()), 
      ipv6=if(ip_version=="ipv6",jndi_domain,null())
    | where match(ip_version,"ipv\d") 
    | rex field=ipv4 "(?<dest_ip>[^\]\:]+)(?:\]|\:)(?<dest_port>\d+)"
    | rex field=ipv6 "(?:\[|^)(?<dest_ip>[^\]]+)(?:$|\](?<dest_port>\d+))"
    | eval dest_port=if(isnull(dest_port) OR len(dest_port)==0,"*",dest_port)
    | fields dest_ip dest_port ] 
| stats c by action dest dest_port src src_port
```

**If you have Splunk ES or just have the Splunk CIM app installed and are using the Network Traffic datamodel the below search can also be used.**
```plain
| tstats summariesonly=t c from datamodel=Network_Traffic where All_Traffic.action!="blocked" AND 
    [| search index=* TERM(jndi) 
    | rex max_match=0 "(?i)jndi\:(?:[^\/]*)\/{1,2}(?<jndi_domain>[^\/\s\,]+)" 
    | stats c by jndi_domain 
    | eval jndi_domain=replace(lower(jndi_domain), ".*?\$\{[a-z0-9-_:\.]+?\}","*"), jndi_domain=trim(jndi_domain,"}"),
      ip_version=case(match(jndi_domain,"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"),"ipv6", match(jndi_domain,"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"),"ipv4", true(),"domain"), 
      ipv4=if(ip_version=="ipv4",jndi_domain,null()), 
      ipv6=if(ip_version=="ipv6",jndi_domain,null())
    | where match(ip_version,"ipv\d") 
    | rex field=ipv4 "(?<dest_ip>[^\]\:]+)(?:\]|\:)(?<dest_port>\d+)"
    | rex field=ipv6 "(?:\[|^)(?<dest_ip>[^\]]+)(?:$|\](?<dest_port>\d+))"
    | eval dest_port=if(isnull(dest_port) OR len(dest_port)==0,"*",dest_port)
    | rename dest_ip AS All_Traffic.dest, dest_port AS All_Traffic.dest_port ] by _time span=1s All_Traffic.action All_Traffic.dest All_Traffic.dest_port All_Traffic.src All_Traffic.src_port
```

### DNS based JNDI connections
Find connection in your DNS logs with query's for a domain that was in the jndi string.

```plain
index=[DNS INDEX] sourcetype=named 
    [| search index=* TERM(jndi) 
    | rex max_match=0 "(?i)jndi\:(?:[^\/]*)\/{1,2}(?<jndi_domain>[^\/\s\,]+)" 
    | stats c by jndi_domain 
    | eval jndi_domain=replace(lower(jndi_domain), ".*?\$\{[a-z0-9-_:\.]+?\}","*"), jndi_domain=trim(jndi_domain,"}"),
      ip_version=case(match(jndi_domain,"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"),"ipv6", match(jndi_domain,"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"),"ipv4", true(),"domain"), 
      ipv4=if(ip_version=="ipv4",jndi_domain,null()), 
      ipv6=if(ip_version=="ipv6",jndi_domain,null())
    | where !match(ip_version,"ipv\d") AND !match(jndi_domain,"^\$") AND !match(jndi_domain,"\}|\:") AND !match(jndi_domain,"\s") AND jndi_domain!="localhost" AND len(jndi_domain)>4 AND match(jndi_domain,".*\..*")
    | fields jndi_domain 
    | rename jndi_domain AS query ]
| stats values(answer) AS answer, values(reply_code) AS reply_code, values(src_category) AS src_category BY _time src_ip query
| table _time src_ip src_category query reply_code answer
```

```plain
| tstats summariesonly=t values(DNS.answer) AS answer, values(DNS.reply_code) AS reply_code, values(DNS.src_category) AS src_category from datamodel=Network_Resolution.DNS where 
    [| search index=* TERM(jndi) 
    | rex max_match=0 "(?i)jndi\:(?:[^\/]*)\/{1,2}(?<jndi_domain>[^\/\s\,]+)" 
    | stats c by jndi_domain 
    | eval jndi_domain=replace(lower(jndi_domain), ".*?\$\{[a-z0-9-_:\.]+?\}","*"), jndi_domain=trim(jndi_domain,"}"),
      ip_version=case(match(jndi_domain,"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"),"ipv6", match(jndi_domain,"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"),"ipv4", true(),"domain"), 
      ipv4=if(ip_version=="ipv4",jndi_domain,null()), 
      ipv6=if(ip_version=="ipv6",jndi_domain,null())
    | where !match(ip_version,"ipv\d") AND !match(jndi_domain,"^\$") AND !match(jndi_domain,"\}|\:") AND !match(jndi_domain,"\s") AND jndi_domain!="localhost" AND len(jndi_domain)>4 AND match(jndi_domain,".*\..*")
    | fields jndi_domain
    | rename jndi_domain AS DNS.query ] by _time span=1s DNS.src DNS.query
```
