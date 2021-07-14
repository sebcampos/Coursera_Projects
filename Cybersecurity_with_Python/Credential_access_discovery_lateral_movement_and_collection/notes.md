# Python for credential access
## Credential Access
* User Credentials can be a very valuable resource for an attacker
    - Expand access to systems, applications and network
    - Elevate permissions on compromised systems
    - Provide persistence and impair detection

* Accessing credentials is a common stage in attacks
    - Credentials can advance the attackers goals
    - Credentials are also valuable commodities for resale

* User credentials are a common defensive weakness with many potential points of compromise
    - Brute Force
    - Credentials from password stores
    - Exploitation for credential Access
    - Forced Authentication
    - Input Capture
    - Man-in-the-Middle
    - Modify Authentication Process
    - Network Sniffing
    - OS credential Dumping
    - Steal application Access Toekn
    - Steal Web Session Cookie
    - Two-Factor authentication interception
    - Unsecured Credentials

## Python for credential access
- Credentials from password stores: credentials from web browsers
- Network sniffing

## Introduction to credentials from password stores
* Systems commonly store user credentials in files of memory
    - website logons
    - User password in RAM

* An attacker may be able to extract these yser credentials for their own use

## Intro to network sniffing
* User credentials are commonly transmitted ober the network:
    - Authentication to remote services
    - Login to web applications

* These credentials are encrypted for most protocols
    - protocol encryption or TLS encryption

* These protections may not always be in place:
    - use of insecure protocols
    - web proxies and TLS interception

see networksniffing.py


# Python for Discovery
## MITRE ATTACK Discovery
* Once present on a network an attacker needs access to a lot of additional information:
    - Systems on the network
    - User accounts and permissions
    - Locations of valuable data and functionality
    - Opportunities for lateral movement

* Most of this information is not available outside of the network:
    - Firewalls and othe solutions block discovery efforts
    - Attackers need to perform discovery from machines inside of the network

* MITRE ATTACK Defines many discovery Techniques:
    - Account Discovery
    - Application Window Discovery
    - Browser Bookmark Discovery
    - Cloud Infrastructure Discovery
    - Cloud Service Dashboard
    - Cloud Service Discovery
    - Domain trust discovery
    - File and directory Discovery
    - Network Service Share Discovery
    - Network Sniffing
    - Password Policy Discovery
    - Peripheral device discovery
    - Permission groups discovery
    - Process Discovery
    - Query registry
    - Remote System discovery
    - Software Discovery
    - System information discovery
    - System network configuration discovery
    - System network connections discovery
    - system owner/user discovery
    - System service discovery
    - system time discovery
    - Virtualization/sandbox evasion

* Python for discovery:
    - Account Discovery: User Account Discovery
    - File and Directory Discovery



## Introduction to account discovery
