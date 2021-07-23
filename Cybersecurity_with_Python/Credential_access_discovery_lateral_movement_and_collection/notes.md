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
* User accounts are abaluable resource for an attacker:
    - privelege escalation
    - lateral movement
    - persistence

* Account discovery helps an attacker to identify potentially usefull accounts:
    - High-privilege accounts are valuable targets
    - Other accounts may be easy to compromise

## Introduction to File and directory Discovery
* Files and adta on a system are central to a number of different types of common attacks
    - data breach
    - ransomware 
    - Credential theft

* File and directory discovery helps to identify high-value data
    - Personally identifiable information (PII)
    - Critical data
    - Authentication information

# Python for Lateral Movement
## MITRE ATTACK Lateral Movement
* An attacker can gain access to an organizations network and system in a variety of different ways
    - Phishing emails
    - Web Applications
    - Supply chain compromise
    - And more

* However these methods rarley place the attacker wherer they need to be to achieve their objectives
    - Compromised systems are usually internet-facing
    - High-value systems are more protected
    - Lateral Movement is required



* An attacker can move laterally through an organizations network via a number of different methods
    - Exploitation if remote services
    - Internal Spearphishing
    - Lateral Tool Transfer
    - Remote Service Session Hijacking
    - Remote Services
    - Replication Through Removable Media
    - Softwar Deployment Tools
    - Taint Shared Content
    - Use Alternate Authentication Material

## Introduction to Use alternative Authentication material
* Users commonly authenticate to sercives using usernames and passwords, ssh keys, etc
    - This is not the only way to authenticate

* Constnantly Entering in usernames and passwords on a system is annoying and inefficent
    - systems will save authentication state to make the system easier to use
    - Attackers can exploit this saved state to expand their access on an organizations network


# Python for Collection
## Collection
* Data is essential to a variety of cyber sttacks and attack objectives
    - Data Breaches
    - Lateral Movesment
    - Privilege escalation

* Once attackers have access to a system, they need to collect any data abailable there 
    - Exfiltrate data for breach
    - Use collected data to inform next steps

## MITRE ATTACK Collection
* Attackers can leverage a number of different sources to collect data bout a system and its users:
    - Archive collected data
    - Audio Capture
    - Automated Collection
    - Clipboard Data
    - Data from Cloud Storage Object
    - Data from configuration Repository
    - Data from Information Repositories
    - Data from local System
    - Data from Network Shared Drive
    - Data from Removeable Media
    - Data Staged
    - Email Collection
    - Input Capture
    - Man-in-the-Browser
    - Man-in-the-middle
    - Screen Capture
    - Video Capture


## Python for collection
- clipboard data
- Email collection

## Introduction to clipboard data
* The system clipboard is a useful tool for transferring data
    - Copy data in one application
    - Past the data in another

* Many of the applications on a system require access to the system clipboard:
    - Any application can be sued for copy/paste
    - All require read/write clipboard access

* An attacker can take advantage of this universal clipboard acess:
    - Read sensitive data from the clipboard
    - Modigy the data stored on the clipboard

## Introduction to email collection
* Emails can be a rich source of data for an attacker:
    - Personally Identifiable Information (PII)
    - Intellectual Property
    - Data about employee relationships

* This data may be stored in multiple different locations accessible to an attacker:
    - Web-based email inboxes
    - local email caches

