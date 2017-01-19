from bs4 import BeautifulSoup
import requests
import re
import pprint
from pymongo import MongoClient

def retrieveSpellNamesFromPaizo():
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

def retrieveSpellDescriptions():
    session = requests.session()

    req = session.get('http://paizo.com/pathfinderRPG/prd/coreRulebook/spellLists.html')
    webpage = req.content
    webpage = webpage.decode('utf-8')

    soup = BeautifulSoup(webpage, "html5lib")

    listOfDescriptions = soup.body.find_all("p")

    for dirtyDescription in listOfDescriptions:
        dirtyDescription.decode('utf-8')
        cleanDescription = dirtyDescription.getText()
        print cleanDescription

    spellDescriptions = []
    SPELL_DESCRIPTIONS = open("speechAssets/customSlotTypes/SPELL_DESCRIPTIONS.txt", "w")

    for string in listOfDescriptions:
        #print string
        spellDescriptions.append(string.contents[0])

    #for spellDescrip in spellDescriptions:
        #SPELL_DESCRIPTIONS.write(spellDescrip+"\n\n")

    SPELL_DESCRIPTIONS.close()

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

#makeConnectionToDatabase()

#retrieveSpellNamesFromPaizo()
retrieveSpellDescriptions()
