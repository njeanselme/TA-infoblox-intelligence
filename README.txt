Splunk Add-on for Infoblox Intelligence allows to get threat intelligence from TIDE (hosts/IPs/URLs - depending on your licenses) and network intelligence from networks in NIOS IPAM. It optionally allows to feed Splunk Entreprise Security (Splunk ES).

Threat Intelligence

Pre-requisite: 
- TIDE api key
- Treemap app - https://splunkbase.splunk.com/app/3118/
- Punchmap - https://splunkbase.splunk.com/app/3129/
 
Set Configuration / Add-on-settings / TIDE API Key with the key obtained from TIDE / https://platform.activetrust.com

- to create a new input configuration, click "Create New Input",  Infoblox threat intelligence domains /  Infoblox threat intelligence IPs /  Infoblox threat intelligence URLs
    - Name: Unique name for the input configuration.
    - Interval: The number of seconds between data collections. 3600 second is recommended
    - Profile: IID is the only option currently supported

Network Intelligence

Network intelligence is based on the network list exported is in CSV including extensible attributes.
The extensible attributes mapped to Splunk Entreprise Security are Owner, SecurityLevel, latitude, longitude, City, Country plus the comment field.
It is highly recommended to create it on NIOS to have full benefit of this integration.

- To create a new input configuration click "Create New Input" / "Infoblox IPAM Networks"
    - Name: Unique name for the input configuration.
    - Interval: The number of seconds between data collections. 3600 second is recommended
    - API URI Base: The URL provided for the Infoblox NIOS grid master. For example: https://infoblox-grid-master.company.internal
    - API version: v2.5 by default
	- Username / Password: credentials for the account that has read access to all networks over WAPI