import dalfileio
import jacknife
import dalmongo
import os

extension = "extension"
name = "name"
rawpath = "rawpath"
parents = "parents"
keys = "keys"
contents = "contents"

databasename = "dbsb"
food = "food"
recipes = "recipes"

modroot = "..\\mods\\"
assetroot = "..\\unpacked\\"

def getFiles(lookIn, forthese):
    
    
    return dalfileio.getFiles(assetroot+lookIn,forthese)

#removes all subfolders of a mod
def clearMod(modname):
   if (modname == ""):
      print ("You almost purged your mod folder!")
      return

   modpath = modroot + modname
   dalfileio.clearDir(modpath)


def getFilesJSON(lookIn, forthese):
    
    return dalfileio.getFilesJSON(assetroot+lookIn,forthese)

def startclient():
   return dalmongo.startclient()

#Deletes the collection if it is pressent
def deleteIfPresent(collectionName, db):
   dalmongo.deleteIfPresent(collectionName,db)

#Sets up the files
def prepmod(modname):
    
    dalfileio.makedirswocomplaining(modroot+modname)

    return True

#Makes directories and supresses exceptions
def makedirswocomplaining(locus):
    dalfileio.makedirswocomplaining(locus)


#Gets the json file from the path
def getjson(locus):
    return dalfileio.filetojson(locus)

def makepatch(forthis,modname,contents):
     modpath = modroot+modname + "\\"
     counter = 2

     while (counter < len(forthis['parents'])):
        modpath = modpath + forthis['parents'][counter] + "\\"
        counter = counter + 1
    
     makedirswocomplaining(modpath)

     modpath = modpath + forthis['name'] + "." + forthis['extension'] + ".patch"

     

     dalfileio.makefile(modpath,contents)

#Returns items with the items in checkeme in its crafting recipe
def itemsMadeWithThese(checkme):
    hasthese = jacknife.ensureArray(checkme)
    leClient = startclient()
    leDB = leClient[databasename]
    lenPrior = len(hasthese)
    lenAfter = -1

    while (lenPrior != lenAfter):
        lenPrior = len(hasthese)
        leRecipeCollection = leDB[recipes].find({"input.item" :{ "$in":hasthese }})
        for rec in leRecipeCollection:
            jacknife.addIfNotThere(rec["output"]["item"],hasthese)
        lenAfter = len(hasthese)

    return hasthese

#Returns true if there is a crafting recipe for checkme (Item or object name)
def isCraftable(checkme):
   leClient = startclient()
   leDB = leClient[databasename]
   query = {"output.item":checkme}
   toSend = leDB[recipes].find_one(query)
   return (jacknife.testForNoneType(toSend) == False)

#Gets a single food item
def getFoodItem(thisone):
   leClient = startclient()
   leDB = leClient[databasename]
   query = {"itemName":thisone}
   toSend = leDB[food].find_one(query)
   return toSend

#Gets food items for a list if item names
def getFoodItems(fromthese):
   grindme = jacknife.ensureArray(fromthese)
   toSend = []

   for ite in fromthese:
      toPut = getFoodItem(ite)

      if (jacknife.testForNoneType(toPut) == False):
         toSend.append(toPut)

   return toSend

def addCheatSheet(modname,contents):
   outputpath = modroot+modname + "\\cheatsheet.txt"
   dalfileio.makefile(outputpath,contents)

#Makes a similar file in the mod
#tocopy = JSON object
#newname = New file name
#newcontents = String contents for file
def createDopple(forthis,modname,newname,contents):
   modpath = modroot+modname + "\\"
   counter = 2

   while (counter < len(forthis['parents'])):
        modpath = modpath + forthis['parents'][counter] + "\\"
        counter = counter + 1
    
   makedirswocomplaining(modpath)

   modpath = modpath + newname + "." + forthis[extension]

   dalfileio.makefile(modpath,contents)

#Gets food and recipes (even non-food ones)
def makedbFoodAndRecipe():
    leClient = startclient()
    leDB = leClient[databasename]
    #Get all food items
    
  
    print ("===Add Food Collection===")

    meat = getFilesJSON("items\\generic\\meat","consumable")["consumable"]
    produce = getFilesJSON("items\\generic\\produce","consumable")["consumable"]
    foodCollection = getFilesJSON("items\\generic\\food","consumable")["consumable"]
    shop = getFilesJSON("items\\generic\\shop","consumable")["consumable"]
    deleteIfPresent(food,leDB)
    foodResults = leDB[food].insert_many(foodCollection)
    meatResults = leDB[food].insert_many(meat)
    produceResults = leDB[food].insert_many(produce)
    shopResults = leDB[food].insert_many(shop)
    totalResults = len(foodResults.inserted_ids) + len(meatResults.inserted_ids) + len(produceResults.inserted_ids) + len(shopResults.inserted_ids)
    print ("Food items added: " + str(totalResults))

    print ("===Add Food Recipie Collection===")
    deleteIfPresent(recipes,leDB)
    allRecipes = getFilesJSON("recipes","recipe")["recipe"]
    recipeResults = leDB[recipes].insert_many(allRecipes)
    print ("Recipes added:" + str(len(recipeResults.inserted_ids)))

def getListOfFoods():
   leClient = startclient()
   leDB = leClient[databasename]
   toSendRaw = leDB[food].find()
   toSend = []

   for a in toSendRaw:
      toPut = a["itemName"]
      toSend.append(toPut)

   return toSend

def dbExists():
   return dalmongo.dbExists(databasename)

#Shuts down the program if 
def safeDBExists():
   try:
      return dbExists()
   except:
      print("Could not check if the db exists. Please ensure MongoDB and pyMongo are installed correctly.")
      exit()

#Ensures the proper files exist
def goodToGo():
   toSend = True
   if (dalfileio.pathExists(modroot) == False):
      print("Please create a folder called \"mod\" in the Starbound directory")
      toSend = False
   
   if (dalfileio.pathExists(assetroot) == False):
      print("Please unpack the Starbound assets and put the \"unpacked\" folder in the Starbound directory")
      toSend = False
   
   return toSend
