#Created By David Schriver in 2019
import allergy
import sbmodio
import jacknife

glutenModname = "glutenAllergy"
glutenAllergens = ["wheat"]

dairyModname = "dairyAllergy"
dairyAllergens = ["milk","cheese"]

diabetesModname = "beetus"
diabetesAllergens = ["sugar"]

veganModName = "vegamism"
veganAllergens = ["alienmeat","rawbacon","rawfish","rawpoultry","rawribmeat","rawtentacle","rawham","egg","milk"]

fishModName = "fishAllergy"
fishAllergens = ["rawfish"]

beetusModName = "diabeetus"
beetusAllergens = ["sugar"]

customAllergyName = "customAllergy"


def makeGlutenAllergy():
    allergy.createAllergy(glutenModname,glutenAllergens)

def makeLactoseAllergy():
    allergy.createAllergy(dairyModname,dairyAllergens)


def makeFishAllergy():
    allergy.createCustomAllergy(fishModName,fishAllergens,allergy.customAllergic)


def makeBeetus():
    allergy.createCustomAllergy(beetusModName,beetusAllergens,allergy.customCombustion)

def makeVeganDiet():
    allergy.createCustomAllergy(veganModName,veganAllergens,allergy.customCombustion)

def makeCustom():
    print("Enter allergen foods separated by commas or enter \"c\" to cancel")
    allergens = input().split(",")

    if (allergens == "c"): return

    validChoices = ["1","2","3","c"]
    allergyType = allergy.allergicReactionAddPatch
    choice = ""
    print ("Select reaction type:")

    
    while (choice not in validChoices):
        jacknife.printAryContents(["1: Intolerance","2: Allergic","3: Spontaneous Combustion", "c: Cancel" ])
        choice = input()

        if (choice == "2"):
            allergyType = allergy.customAllergic
        if (choice == "3"):
            allergyType = allergy.customCombustion
        if (choice == "c"):
            return

    modName = ""

    while (modName == ""):
        print("Please select a valid name for this mod")
        modName = input()

    #Create The allergy
    allergy.createCustomAllergy(modName,allergens,allergyType)


    

def makeVeganism():
    #1: Create allergy to animal products
    nonveganitems = allergy.createCustomAllergy(veganModName,veganAllergens,allergy.customCombustion)
    
    #2: Create vegan alternatives to animal products (Both base and crafted). All effects should be reduced by some percentage
    multiplier = 0.9
    wrdVegan = "Vegan"
    genericExplanation = "A plant based alterantive to animal cruelty."
    
    for a in nonveganitems:
        toPut = a
        toPut["itemName"] = "vegan" + toPut["itemName"]
        toPut["shortdescription"] = wrdVegan + " " + toPut["shortdescription"].replace("'","APOHERE")
        toPut["description"] = toPut["description"].replace("'","APOHERE")

        if (a["itemName"] in veganAllergens):
            toPut["description"] = genericExplanation

        del toPut["_id"]
        del toPut["name"]
        del toPut["rawpath"]
        sbmodio.createDopple(a,veganModName,toPut["itemName"],str(toPut).replace("'","\"").replace("APOHERE","'"))

    #3: Create vegan recipes
        #TODO
    #4: Make vegan recipes available
        #TODO