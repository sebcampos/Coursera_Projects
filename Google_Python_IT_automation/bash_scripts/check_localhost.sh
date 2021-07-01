#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
	echo "Local host confirmed"
else
	echo "ERROR local host not found in /etc/hosts"
fi
