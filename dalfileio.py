import os
import json
import shutil

extension = "extension"
name = "name"
filename = "filename"
rawpath = "rawpath"
parents = "parents"
keys = "keys"
contents = "contents"

#Gets an object containing information about the file name and its location
#fromDir(String): The path to look in
#exts(String Array): A set of extensions to extract
def getFiles(fromDir, exts):
#Example input:
# fromDir = "..//unpacked//items"
# exts = ["consumable"]
#Example Output: {"consumable"[{
#           'extension': 'consumable',
#           'name': 'bakedpotato', 
#           'rawpath': '..\\unpacked\\items\\generic\\food\\tier1\\bakedpotato.consumable', 
#           'parents': ['..', 'unpacked', 'items', 'generic', 'food', 'tier1']}]}

    #Array or string
    toGrind = []
    toSend = {}
    if (type(exts) == str):
        toGrind.append(exts)
    elif(type(exts) == list):
        toGrind = exts
    else:
        print("ERROR: Second parameter must be a single string or a list")
        return

    for s in toGrind:
        toSend[s] = []

    if (type(fromDir) != str):
        print("ERROR: First parameter must be a string!")
        return
    
    #Get the files
    rawPaths = os.walk(fromDir)

    for path, folders, files in rawPaths:
        for n in files:
            splitN = n.split(".")
            toAdd = {}
            toAdd[extension] = splitN[len(splitN) - 1]
            toAdd[name] = splitN[0]
            toAdd[rawpath] = path + "\\" + n
            toAdd[parents] = path.split("\\")
            
            if (toGrind.__contains__(toAdd[extension])):
                toSend[toAdd[extension]].append(toAdd)
    
    toSend[keys] = toGrind
    
    return toSend

#empties the directory but leaves the contents of the root untouched BE CAREFUL WITH THIS!
def clearDir(delpath):
     rawPaths = os.walk(delpath)

     for paths, folders, files in rawPaths:

         if (paths != delpath):
            shutil.rmtree(paths)

#Gets the json files and adds the file information to it
def getFilesJSON(fromDir, exts):
    #Array or string

    toGrind = []
    if (type(exts) == str):
        toGrind.append(exts)
    elif(type(exts) == list):
        toGrind = exts
    else:
        print("ERROR: Second parameter must be a single string or a list")
        return

    if (type(fromDir) != str):
        print("ERROR: First parameter must be a string!")
        return

    toAddTo = getFiles(fromDir,exts)

    for ex in toGrind:
        for obj in toAddTo[ex]:
            leIndex = toAddTo[ex].index(obj)
            toPut = filetojson(toAddTo[ex][leIndex][rawpath])
            toPut[extension] = obj[extension]
            toPut[name] = obj[name]
            toPut[rawpath] = obj[rawpath]
            toPut[parents] = obj[parents]
            toAddTo[ex][leIndex][contents] = filetojson(toAddTo[ex][leIndex][rawpath])
            toAddTo[ex][leIndex] = toPut
            

    
    return toAddTo



#Will make a direcctory without whining when it discovers the folder is already there
def makedirswocomplaining(locus):
    try:
        os.makedirs(locus)
    except:
        f=1

#Takes a file path (locus) and gets it as a JSON object
def filetojson(locus):
    rawFile = open(locus, "r")
    jsonText = ""
    foundMultilineComment = False
    for ln in rawFile:
        
        #Add the line if it isn't in a comment
        #https://stackoverflow.com/questions/663171/how-to-substring-a-string-in-python

        if (ln.find("/*") != -1):
            foundMultilineComment = True

        if (ln.find("//") == -1 and foundMultilineComment == False):
            jsonText = jsonText + ln + "\n"
        elif(ln.find("//")  != -1):
            #If it finds a full line comment cut the line to that comment
            jsonText = jsonText + ln[0:ln.find("//"):1]

        if (ln.find("*/") != -1):
            foundMultilineComment = False

    rawFile.close()
    toSend = ""

    try:
        toSend = json.loads(jsonText)
    except:
        print("ERROR:CANNOT PARSE " + locus)
        print(locus)
        return {"brokenPath":locus}

    return toSend

#Takes the full path 
def makefile(locus,contents):
    newfile = open(locus,"w")
    newfile.write(contents)
    newfile.close()

def pathExists(locus):
    return os.path.exists(locus)
            