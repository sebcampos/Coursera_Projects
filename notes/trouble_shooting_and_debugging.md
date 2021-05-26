# Trouble Shooting and Debugging


## Possible causes of slowness
- look for simplest explanations
- look for WHEN computer is slow
- if a computer is slow on start up it could be too many apps on boot
- if computer is slow after running for a few days then it could be one programs that is logging data without properly managing the data
- Another reason for slowness could be that a programs files have become too large for the program to manage such as a extremely large log file

## Slow Web Server
- the `ab` command ie `ab -n 500 site.example.com` will send 500 requests to a website and return stats on the data being sent and returned and is a good way to troubleshoot how your website or a website is behaving

## Slow Code
- python dictionaries are faster than python lists when it comes to retrieveing elements by name

- using the `time` command before calling a command will return the user, system, and cpu usage associated with that command ie `time python_script.py`

- Running a script in parallel allows for short processes to run quickly while a longer process is being run instead of the traditional linear method of one after another. Although this can be time efficient one should be aware that it could be CPU intensive: another word for this is concurency modules that help run scripts in parallel is the `futures module`

- running asynchronous events can be done with the asyncio module

