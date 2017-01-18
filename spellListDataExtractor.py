from bs4 import BeautifulSoup
import requests
import re
import pprint
from pymongo import MongoClient

def retrieveSpellsFromPaizo():
    session = requests.session()

    req = session.get('http://paizo.com/pathfinderRPG/prd/coreRulebook/spellLists.html')
    webpage = req.content

    wepage = webpage.decode('utf-8')

    soup = BeautifulSoup(webpage, "html5lib")

    listOfSpells = soup.body.find_all("a", href=re.compile('^spells/*'))

    spellNames = []
    LIST_OF_SPELLS = open("speechAssets/customSlotTypes/LIST_OF_SPELLS.txt", "w")

    for string in listOfSpells:
        spellNames.append(string.contents[0])

    for spell in spellNames:
        if isinstance(spell, basestring) == True:
            spell = spell.lower()
            LIST_OF_SPELLS.write(spell+"\n")


    LIST_OF_SPELLS.close()

def makeConnectionToDatabase():
    LIST_OF_SPELLS = open("speechAssets/customSlotTypes/LIST_OF_SPELLS.txt", "r")

    client = MongoClient()
    db = client.testCollection

    spellsInDatabase = db.spellsInDatabase

    for line in LIST_OF_SPELLS:
        post = {"spell": line,
                "description": ""}
        spellsInDatabase.insert_one(post)

    for spell in spellsInDatabase.find():
        pprint.pprint(spell)

makeConnectionToDatabase()

#retrieveSpellsFromPaizo()
