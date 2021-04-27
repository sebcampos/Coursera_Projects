#!/bin/bash


line='----------------------------------------'

echo "Starting at: $(date)"
echo $line

echo "UPTIME"
echo $line
uptime
echo $line

echo "WHO"
who
echo $line

echo "Finishing at $(date)"


