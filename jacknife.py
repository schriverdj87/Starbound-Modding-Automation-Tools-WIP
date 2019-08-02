#Ensures that an array stays an array and a single variable remains a variable
def ensureArray(grindme):
    if(type(grindme) == list):
        return grindme

    return grindme

#Adds an element if it is not already in the db
def addIfNotThere(addme, tothis):
    if ((addme in tothis) == False):
        tothis.append(addme)

#Reads the contents of an array
def printAryContents(grindme):
    toread = ensureArray(grindme)

    for a in toread:
        print(a)

#It's difficult to test for "NoneType" otherwise
def testForNoneType(testme):
    return (str(type(testme)) == "<class 'NoneType'>")

#Handles the KeyError exception for you by returning "EMPTY"
def safeJSONGet(fromThis, key):
    try:
        toSend = fromThis[key]
        return toSend
    except KeyError:
        return "EMPTY"

#Handles the KeyError exception for you by returning "EMPTY"
def safeJSONGetDefineEmpty(fromThis, key, empty):
    try:
        toSend = fromThis[key]
        return toSend
    except KeyError:
        return empty