import os
import re
import sys

def renameFile(fullFilePath, intIndex):
    if intIndex < 10:
        index = str(f"0{intIndex}")
    else:
        index = str(f"{intIndex}")

    fpSplit = fullFilePath.split("/")
    oldFileName = fpSplit[-1]
    del fpSplit[-1]
    path = ""
    for s in fpSplit:
      path += s
      path += "/"

    x = oldFileName.split(" - ")
    newFileName = (f"{index}. {x[1]} - {x[2]}")
    newFileName = re.sub(" \[.*?\]", "", newFileName)

    newFile = (f"{path}{newFileName}")
    os.rename(fullFilePath, newFile)

def main():
    if(len(sys.argv) != 2):
        print("Path required")
    else:
        fullFilePath = str(sys.argv[1])
        newFileIndex = 1
        while True:
            os.system('cls')
            dirContents = os.listdir(str(sys.argv[1]))
            fileIndex = 1
            for f in os.listdir(fullFilePath):
                if f.endswith(".mp3"):
                    print(f"{fileIndex} - {f}")
                    fileIndex += 1

            try:
                indexToRename = int(input(">_ "))
            except ValueError: 
                print("Exiting...")
                sys.exit(0)
            indexToRename = indexToRename - 1
            if indexToRename <= fileIndex:
                fileToRename = (f"{fullFilePath}/{dirContents[indexToRename]}")
                renameFile(fileToRename, newFileIndex)

                # del fileList[indexToRename]
                newFileIndex += 1
            else:
                print("Please select a valid value")


main()
