import sbmodio
import jacknife



allergicReactionPatch = '''
[
    {
        "op":"replace",
        "path":"/effects",
        "value": [ [
          {
            "effect" : "foodpoison"
          }
        ] ]
    }
]
'''

allergicReactionAddPatch = '''
[
    {
        "op":"add",
        "path":"/effects",
        "value": [ [
          {
            "effect" : "foodpoison"
          }
        ] ]
    }
]
'''

allergicReactionPatchCustom = '''
[
    {
        "op":"replace",
        "path":"/effects",
        "value": [ [
          CUSTOM
        ] ]
    }
]
'''

allergicReactionAddPatchCustom = '''
[
    {
        "op":"add",
        "path":"/effects",
        "value": [ [
          CUSTOM
        ] ]
    }
]
'''
#Turns the player red and poisons them for 400 seconds
customAllergic = '''
    { "effect" : "colorred", "duration": 30},
    { "effect" : "weakpoison", "duration": 400}
'''

customCombustion = '''
    { "effect" : "melting", "duration" : 400}
'''

def createAllergy (modname,allergicTo):
    prepMod(modname)
    allergenFoods = getItemsMadeWithAllergens(allergicTo)
    createPatches(modname,allergenFoods)
    makeCheatSheet(modname,allergenFoods)
    print("Allergy mod created successfully! You should find it in mods/" + modname)
    return allergenFoods

def createCustomAllergy(modname, allergicTo, effects):
    prepMod(modname)
    allergenFoods = getItemsMadeWithAllergens(allergicTo)
    createCustomPatches(modname,allergenFoods,effects)
    makeCheatSheet(modname,allergenFoods)
    print("Allergy mod created successfully! You should find it in mods/" + modname)
    return allergenFoods

#Clear the mod directory and ensure it exists
def prepMod(modname):
    sbmodio.clearMod(modname)
    sbmodio.prepmod(modname)

#Get the item objects that were made with the allergens
def getItemsMadeWithAllergens(allergicTo):
    foodNames = sbmodio.itemsMadeWithThese(allergicTo)
    toSend = sbmodio.getFoodItems(foodNames)
    return toSend


def createPatches(modname,forthese):
    for obj in forthese:
        patchToPut = allergicReactionPatch

        #If it doesn't have an effect then add it
        try:
            test = obj["effects"]
        except KeyError:
            patchToPut = allergicReactionAddPatch

        sbmodio.makepatch(obj,modname,patchToPut)

def createCustomPatches(modname,forthese,effects):
    for obj in forthese:
        patchToPut = allergicReactionPatchCustom.replace("CUSTOM",effects)

        #If it doesn't have an effect then add it
        try:
            test = obj["effects"]
        except KeyError:
            patchToPut = allergicReactionAddPatchCustom.replace("CUSTOM",effects)

        sbmodio.makepatch(obj,modname,patchToPut)

def makeCheatSheet(modname,forthese):
    cheatsheetContents = ""
    for obj in forthese:
        cheatsheetContents = cheatsheetContents + obj["shortdescription"] + " / " + obj["itemName"] + "\n"
    
    sbmodio.addCheatSheet(modname,cheatsheetContents)
