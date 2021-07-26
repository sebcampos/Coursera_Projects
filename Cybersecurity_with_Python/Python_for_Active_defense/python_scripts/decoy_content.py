import pathlib

def getTimeStamps(filename):
    fname = pathlib.Path(filename)
    stats = fname.stat()
    if not fname.exists(): #file detected
        return []
    return(stats.st_ctime, stats.st_mtime, stats.st_atime)


def checkTimeStamp(filename, create, modify, access):
    stats = getTimeStamps(filename)
    if len(stats) == 0:
        return False # file was deleted
    (ctime, mtime, atime) = stats
    if float(create) != float(ctime):
        return False # file creation time is incorrect
    elif float(modify) ! = float(mtime):
        return False # file modify time is incorrect
    elif float(access) != float(atime):
        return False # file access time is incorrect
    return True

def checkDecoysFiles():
    with open("decoys.txt","r") as f:
        for line in f:
            vals = line.rstrip().split(",")
            if not checkTimeStamps(vals[0], vals[1], vals[2], vals[3]):
                print(f"{vals[0]} has been tampered with")

checkDecoysFiles()