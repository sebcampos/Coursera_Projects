#!/usr/local/bin/python3
import os
import shutil
import sys
import socket
import psutil

def check_reboot():
	'''Returns True if the computer has a pending reboot.'''
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	'''Returns True if there isn't enough disk space, False otherwise.'''
	du = shutil.disk_usage(disk)
	#calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	#calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if gigabytes_free < min_gb or percent_free < min_percent:
		return True
	else:
		return False

def check_root_full():
	'''returns True if the root partition if full, False otherwise.'''
	return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
	'''Returns True if if fails to resolve Google's URL, False otherwise'''
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def check_cpu_usage():
	'''Returns True if the cpu is hacing too much usage, False otherwise.'''
	return psutil.cpu_percent(1) > 75


def main():
	checks = [
		(check_reboot, "Pending Reboot"),
		(check_root_full, "Root partition full"),
		(check_no_network, "No working network"),
		(check_cpu_usage, "Cpu Usage ERROR")
	]
	everything_ok = True
	for check, msg in checks:
		if check():
			print(msg)
			everything_ok = False
	if not everything_ok:
		sys.exit(1)
	
	elif everything_ok == True:
		print("All checks Passed:\nReboot check\nRoot Disk Check\nNetwork Check\nCPU usage Check")

main()
