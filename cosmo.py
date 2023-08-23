import json

def readObj() -> list:
    try:
        with open("database.json","r") as file:
            return json.load(file)
    except:
        database = []
        return database
def saveJsonObj(arr_database: list) -> None:
    with open("database.json","a") as file:
        json.dump(arr_database, file)
def addJsonObj(arr_database: list) -> None:
    print("database of cosmo object")
    _id = input(" id-> ")
    print(" coordinate -> ")
    x = int(input(" x -> "))
    y = int(input(" y -> "))
    z = int(input(" z -> "))
    _type = input(" type -> ")
    _name = input(" name -> ")

    new_obj = {
    '_idObj': _id,
    'xPos': x,
    'yPos': y,
    'zPos': z,
    'typeObj': _type,
    'nameObj': _name
    }
    arr_database.append(new_obj)

def findByid(_id):
    print("database of cosmo object")
    database = [{"_id": "d01", "cordX": 555, "cordY": 777, "cordZ": 888, "Type": "Cometa", "Name": "Cometa Halley"}]
    for obj in database:
        if obj["_id"] == _id:
            print(obj)
            return obj

    print("Object with ID '{}' not found.".format(_id))
    return None

object_id = "d01"
found_object = findByid(object_id)

def getAll():
    print("database of cosmo object")
    database = [
        {"_id": "d01", "cordX": 555, "cordY": 777, "cordZ": 888, "Type": "Cometa", "Name": "Cometa Halley"}
    ]
    for obj in database:
        print("Object ID:", obj["_id"])
        print("Coordinates (X, Y, Z):", obj["cordX"], obj["cordY"], obj["cordZ"])
        print("Type:", obj["Type"])
        print("Name:", obj["Name"])
        print("-" * 30)
getAll()

def delitAll():
    global database
    database = []
    print("All objects deleted from the database.")

database = readObj()
addJsonObj(database)
saveJsonObj(database)
getAll()
delitAll()
