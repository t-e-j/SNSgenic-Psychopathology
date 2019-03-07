from subprocess import call
import json
import os
WORKING_DIRECTORY = "/Users/jgann/SEworkingdir/"
errorlog = open("userExtractionErrorLog","w")
processedFiles = open("processedFiles", "w")
usersFile = open("mentalHealthUsers", "w")

subreddits = set(["depression",
                  "mentalhealth",
                  "traumatoolbox",
                  "bipolarreddit",
                  "bpd",
                  "ptsd",
                  "psychoticreddit",
                  "eatingdisorders",
                  "stopselfharm,",
                  "hardshipmates",
                  "panicparty",
                  "socialanxiety"])

def decompressFileAndPlaceInWorkingDirectory(filePath):
    fileName = filePath.split("/")[-1]
    call("cp " + filePath + " " + WORKING_DIRECTORY + fileName, shell=True)
    if ".xz" in fileName:
        call("unxz "+ WORKING_DIRECTORY + fileName, shell=True )
        fileName = fileName[:-3]
    elif ".bz2" in fileName:
        call("bunzip2 " + WORKING_DIRECTORY + fileName, shell=True)
        fileName = fileName[:-4]
    return WORKING_DIRECTORY + fileName

def extractUsefulData(blob):
    subreddit = blob["subreddit"].lower()
    if subreddit in subreddits:
        return (subreddit, blob["author"])

def processFile(filePath):
    writeData = []
    with open(filePath,"r") as f:
        for line in f:
            blob = json.loads(line)
            info = extractUsefulData(blob)
            if info:writeData.append(info)
        writeData = [info[0] + " " + info[1] for info in writeData]
        usersFile.write("\n".join(writeData))
        processedFiles.write(filePath + "\n")
        usersFile.flush()
        processedFiles.flush()

def fileSortKey(fileName):
    year = int(fileName.split("_")[1].split("-")[0])
    month = int(fileName.split("-")[1].split(".")[0])
    return year + month/13.0

files = os.listdir(os.getcwd())
files = [file for file in files if ".bz2" in file or ".xz" in file]
files.sort(reverse=True, key=fileSortKey)
for file in files:
    unpackedFile = decompressFileAndPlaceInWorkingDirectory(file)
    processFile(unpackedFile)
    print file

processedFiles.close()
usersFile.close()
errorlog.close()
