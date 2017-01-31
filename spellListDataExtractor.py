from bs4 import BeautifulSoup
import requests
import re
import pprint
import json
from pymongo import MongoClient

def retrieveSpellNamesFromPaizo():
    session = requests.session()

    req = session.get('http://paizo.com/pathfinderRPG/prd/coreRulebook/spellLists.html')
    webpage = req.content

    wepage = webpage.decode('utf-8')

    soup = BeautifulSoup(webpage, "html5lib")

    listOfSpells = soup.body.find_all("a", href=re.compile('^spells/*'))

    spellNames = []
    LIST_OF_SPELLS = open("LIST_OF_SPELLS.txt", "w")

    for string in listOfSpells:
        spellNames.append(string.contents[0])

    spellsAlreadySeen = set()

    for spell in spellNames:
        spell = spell.lower()
        if spell not in spellsAlreadySeen:
            if isinstance(spell, basestring) == True:
                LIST_OF_SPELLS.write(spell+"\n")
                print spell
                spellsAlreadySeen.add(spell)

    LIST_OF_SPELLS.close()

def retrieveSpellDescriptions():
    session = requests.session()

    req = session.get('http://paizo.com/pathfinderRPG/prd/coreRulebook/spellLists.html')
    webpage = req.content
    webpage = webpage.decode('utf-8')

    soup = BeautifulSoup(webpage, "html5lib")

    listOfDescriptions = soup.body.find_all("p")

    SPELL_DESCRIPTIONS = open("speechAssets/customSlotTypes/SPELL_DESCRIPTIONS.txt", "w")

    for dirtyDescription in listOfDescriptions:
        cleanDescription = dirtyDescription.getText().encode("utf-8")
        SPELL_DESCRIPTIONS.write(cleanDescription+"\n")

    SPELL_DESCRIPTIONS.close()

def makeSpellDescriptionsLowerCase():
    updatedSpellDescriptions = []

    file = open("speechAssets/customSlotTypes/SPELL_DESCRIPTIONS.txt", "r+")
    SPELL_DESCRIPTIONS = file.readlines()

    for upperCaseDescrip in SPELL_DESCRIPTIONS:
        lowerCaseDescrip = upperCaseDescrip.lower()
        print lowerCaseDescrip
        updatedSpellDescriptions.append(lowerCaseDescrip)

    file.seek(0)
    file.truncate()

    for spellDescripToWrite in updatedSpellDescriptions:
        file.write(spellDescripToWrite)

    file.close()

def convertDataToJavaScriptVar():
    SPELL_DESCRIPTIONS_FILE = open("SPELL_DESCRIPTIONS.txt", "r")

    spellList = SPELL_DESCRIPTIONS_FILE.readlines()
    spellListWithDescription = []

    SPELL_DESCRIPTIONS_FILE.close()

    for spell in spellList:
        splitSpell = spell.partition(':')
        spellListWithDescription.append(splitSpell)

    data = []

    for spell in spellListWithDescription:
        print("'" + spell[0] + "': " + "'" + spell[2].strip() + "'," + "\n")
        data.append("'" + spell[0] + "': " + "'" + spell[2].strip() + "'," + "\n")

    javaScriptSpellFile = open("SPELL_LIST.txt", "w")

    for spell in data:
        javaScriptSpellFile.write(spell)

    javaScriptSpellFile.close()

retrieveSpellNamesFromPaizo()
#retrieveSpellDescriptions()
#makeSpellDescriptionsLowerCase()
#convertDataToJavaScriptVar()
