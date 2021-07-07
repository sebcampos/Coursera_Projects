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