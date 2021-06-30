#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def main():
    os.chdir("supplier-data/descriptions")
    data = []
    for item in os.listdir():
        if ".txt" in item:
            with open(item,"r") as opened:
                lst = opened.read().split("\n")
                data.append("name:{}<br></br>weight:{}<br></br><br></br>")
    return "".join(data)


if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", datetime.datetime.now().date().strftime("%B %-d %Y"), main())
    message = emails.generate_email()
    emails.send_email(message)
