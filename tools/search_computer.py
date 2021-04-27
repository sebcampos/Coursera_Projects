#!/usr/bin/python3

import os
import sys

def search_computer(filename, root="/"):
    matches = 0
    for root, dirs, files in os.walk(root, topdown=False):
        if filename in root.lower():
            print(f"{filename} Found at {root}")
            matches+=1  
        for directory in dirs:
            if filename in directory.lower():
                print(f"{filename} Found at {root}")
                matches+=1
        for f in files:
            if filename in f.lower():
                print(f"{filename} Found at {root}: {f}")
                matches+=1
    
    if matches > 0:
        return "\n\nComplete"
    return "File Not Found"
    
try:
    print(search_computer(sys.argv[1], sys.argv[2]))
except IndexError:
    print(search_computer(sys.argv[1]))


