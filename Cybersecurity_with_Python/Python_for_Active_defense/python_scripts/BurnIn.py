import random, requests
from time import sleep

def makeRequest(url):
    _ = requests.get(url)
    return

def getURL():
    return sites[random.randint(0, len(sites)-1)].rstrip()

clickthrough = .5
sleeptime = 1

def browsingSession():
    while (random.random() < clickthrough):
        url = getURL()
        makeRequest(url)
        sleep(random.randint(0,sleeptime))


with open("sites.txt","r") as f:
    sites = f.readlines()


browsingSession()