import pymongo

def startclient():
    return pymongo.MongoClient("mongodb://localhost:27017/")

#Deletes the collection if it is present
def deleteIfPresent(collectionName, db):
    if (collectionName in db.list_collection_names()):
        db[collectionName].drop()


def dbExists(thisname):
    leClient = startclient()
    return (thisname in leClient.list_database_names())
