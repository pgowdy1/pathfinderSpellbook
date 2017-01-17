from bs4 import BeautifulSoup
import requests
import re

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
