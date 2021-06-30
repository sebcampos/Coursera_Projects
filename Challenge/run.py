#!/usr/bin/env python3

import os
import requests

def main():
    os.chdir("supplier-data/descriptions")
    data = []
    for item in os.listdir():
        if ".txt" in item:
            with open(item,"r") as new_file:
                lst = new_file.read().split("\n")
                data.append({
                        "name":lst[0].strip(),
                        "weight":int(lst[1].strip().replace(" lbs","")),
                        "description":lst[2].strip(),
                        "image_name": item.replace(".txt",".jpeg")
                    })
    for dictionary in data:
        r = requests.post("http://34.135.62.230/fruits/", data=dictionary)
        print("{} posted with code {}".format(dictionary["name"], r))


main()
