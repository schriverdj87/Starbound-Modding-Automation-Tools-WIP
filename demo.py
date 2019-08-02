#Created By David Schriver in 2019
import allergyWrangler
import sbmodio
import jacknife

#Make sure everything is properly set up

if (sbmodio.safeDBExists() == False):
    try:
        print("Creating Database")
        sbmodio.makedbFoodAndRecipe()
    except:
        print("Error creating database. Please ensure that MongoDB and pyMongo are properly installed")
        exit()

if (sbmodio.goodToGo() == False):
    exit()



print ("===Welcome Food Allergy Creation Demo===")

choice = ""

while (choice != "q"):
    jacknife.printAryContents(["Please make a selection:","1: Create Gluten Intolerance","2: Create Lactose Intolerance","3: Create Fish Allergy", "4: Create Type Infinity Diabetes","5: Make Custom Allergy","list: Show List Of Foods","db: Refresh/Rebuild Mongo Database","q: Quit"])
    choice = input()

    if (choice == "1"):
        allergyWrangler.makeGlutenAllergy()
    if (choice == "2"):
        allergyWrangler.makeLactoseAllergy()
    if (choice == "3"):
        allergyWrangler.makeFishAllergy()
    if (choice == "4"):
        allergyWrangler.makeBeetus() #Diabetes isn't an allergy, I know!
    if (choice == "5"):
        allergyWrangler.makeCustom()
    if (choice == "list"):
        toRead = sbmodio.getListOfFoods()
        jacknife.printAryContents(toRead)
    if (choice == "db"):
        sbmodio.makedbFoodAndRecipe()

    