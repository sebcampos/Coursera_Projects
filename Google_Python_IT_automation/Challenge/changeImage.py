#!/usr/bin/env python3

import os
from PIL import Image

def main():
    os.chdir("supplier-data/images")
    for item in os.listdir():
        if ".tiff" in item:
            file_name = item.replace(".tiff","")
            Image.open(item).resize((600,400)).convert("RGB").save(file_name+".jpeg","jpeg")
            os.remove(item)
            print("{} removed and saved again".format(item))


main()
