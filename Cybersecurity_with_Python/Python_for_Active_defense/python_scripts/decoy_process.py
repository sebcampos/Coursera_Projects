#!/usr/local/Caskroom/miniconda/base/envs/cybersecurity/bin/python

import signal, sys
from time import sleep


def terminated(signum, frame):
    pass

#catching any commands throwing SIGTERM, SIGINT, kill etc
#if a process attemted to kill this process we can log what sent the signal
#SIGKILL is an uncatchable signal (will not work with this)
signal.signal(signal.SIGTERM, terminated)
signal.signal(signal.SIGINT, terminated)

while True:
    #only availabe on UNIX (signal.sigwait)
    siginfo = signal.sigwaitinfo((signal.SIGINT, signal.SIGTERM))
    with open("terminated.txt","w") as f:
        f.write(f"Process terminated by {siginfo.si_pid}\n")
    sys.exit(0)
