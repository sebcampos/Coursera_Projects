#!/usr/bin/env python3
import requests
import os

def main():
    os.chdir("supplier-data/images")
    url = "http://localhost/upload/"
    for image in os.listdir():
        if ".jpeg" in image:
            with open(image, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                print("{} uploaded with response {}".format(image, r))


main()
