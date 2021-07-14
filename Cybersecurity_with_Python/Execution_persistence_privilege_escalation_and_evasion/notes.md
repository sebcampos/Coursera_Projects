# MITRE ATTACK: Execution
* Most attacks require some form of malicious code execution on a target system:
    - Malware/Malicious scripts
    - Malicious commands used in injection
    - Remote terminal commands

* The execution tactic of MITRE ATTACK focuses on achieveing initial execution:
    - This may be the only stage of execution
    - May only be designed to run a malware dropper or downloader

* An attacker can achieve execution on a target system through a variety of different means:
    - Command and scripting interpreter
    - Exploitation for Client Execution
    - Inter-Process Communication
    - Native API
    - Scheduled Task/Job
    - Shared Modules
    - Software deployment tools
    - System Services
    - User Execution
    - Windows management Instrumentation

## Python for Execution
1. User execution: Malicious links
2. Scheduled Task/jobs: Scheduled Execution


### User Execution
* The end user is a common and good target for a cybercriminal
    - Users are easier to trick than technical defenses
    - A user account may have the permissions that the attacker needs for their attack

* Social Engineering attacks are designed to convince a user to take a dangerous action
    - Clicking a malicious link
    - Opening a malicious file

### Malicious links 
see server.py

### Scheduled tasks and jobs
* All operating systems enable tasks scheduling
    - allow system to perform routine tasks
    - Makes system administration easier

* An attacker can also take advantage of task scheduling
    - Scheduled task can download or drop malware
    - Fileless malware can be written into a scheduled task

### Scheduled execution
see sched.py

## Python for persistence

### Persistence 
* once an attacker gains access to a system they want to maintain this access
    - may have taken a significant investment of time and resources to gain access
    - Cyber defenders actively work to identify and remediate infections
* persistence mechanisms help to maintain an attackers acces
    - resinstall malware if deleted
    - restore execution if terminated
    - persistence mechanisms are concealed on the system

* A number of different operating system tools can be exploited to maintain persistence on a system
    - account manipulation
    - BITS jobs
    - Boot or logon Autostart execution
    - Boot or logon initialization scripts
    - Browser extensions
    - compromise client software binary
    - create account 
    - create or modify system process
    - event triggered execution
    - external remote services
    - hijack execution flow
    - implant container image
    - office application startup
    - pre-OS boot
    - scheduled task/job
    - server software component
    - traffic signaling
    - valid accounts

* Python
    - Boot or Logon Autostart execution: Registry Autorun
    - Hijack Execution Flow: Modified Path

### Boot or autostart execution
* Many different system processes are run on boot or logon
    - Run the processes needed by the system
    - configure the user profile
    - user applications wanting to always be running

* Malware can take advantage of this autorun functionality
    - Add malware binaries or script code to autorun

see autorun.py + create_USB.py


### Hijack execution flow
* Malware can achieve persistence by cuasing it to be run instead of legitimate system processes

* this can be accomplished in a number of different ways 
    - changing system path
    - Exploiting DLL search order


## Python for Priveledge Escalation

* Cybercriminals dont always gain the access that they need to perform their attack
    - most exploits target user workstations or firewalled systems
    - targets may not have high-privilege accounts
    - Compromised accounts may not allow lateral movement

* Privilege escalation anables an attacker to gain the permissions that they need
    - access to higher-level accounts
    - Expanding ther permissions of a compromised account

* MITRE ATTACK outlines several techniques for performing privilege escalation:
    - Abuse elevation control mechanism
    - Access token manipulation
    - boot or lgoon autostart execution
    - boot or logon initialization scripts
    - create or modify system process
    - event triggered execution
    - explotation for pebilege escalation
    - group policy modification
    - hijack execution flow
    - process injection
    - scheduled task/job
    - valid accounts

### Python for privilege escalation
* Python
    - Boot or logon autostart execution: Logon scripts
    - Process Injection: python library injection

### Boot or logon autostart
* Boot and logon autostart can be used to achieve persistence on a system

* It can also be used to perform privilege escalation:
    - Cause malicious code to be loaded by a higher-privilege process
    - Cause malware to be run by a more powerful user account

see script LogonScript.py

### Project injection
* Many application are reliant on third-party code:
    - DLLs
    - Libraries
    - External applications

* These dependencies can be used for privilege escalation
    - Replace a legitimate dependency with a malicious version
    - Higher-privilege process loads and runs the malicious library