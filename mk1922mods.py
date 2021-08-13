# mk1922mods.py

""" 
Make files/directories for hist1922 mods.

Run this once to create:

* file `hist1922_{country}_{w}{v}.md` = mod description file
* corresponding direcry (with same filename)

"""

import butil
from butil import form, prn
from config import MODS_DIR

COUNTRIES = [
    ("france", "France"),
    ("germany", "Germany"),
    ("italy", "Italy"),
    ("japan", "Japan"),
    ("uk", "UK"),
    ("usa", "USA"),
    ("ussr", "USSR"),
]


MOD_FILE_TEMPLATE = """\
# hist1922_{cowv} = historial legacy fleets, 1922, {cocap}, {wPlusV}

Playing as a 1922 start as {cocap}.

The Washington Naval Treaty is {washNot}in effect.
The Versailles Treaty is {versNot}in effect.

Works with the `hist1922` (Historical 1922) mod.

See the [hist1922](hist1922.md) documentation for details.

"""

#---------------------------------------------------------------------

def makeMod(co: str, cocap: str, wash: bool, vers: bool):
    """ make a modiification 
    co = country name (all lower case)
    cocap = country name, capitalised
    wash = is Washington Naval Treaty in force?
    vers = os Versailles Treaty in force?
    """
    washVersStr = (""
        + ("w" if wash else "")
        + ("v" if vers else ""))
    if washVersStr:
        washVersStr = "_" + washVersStr
        
    fnStub = "hist1922_" + co + washVersStr
    fn = fnStub + ".md"
    prn("{}: making file <{}>", cocap, fn)
    modFilePan = butil.join(MODS_DIR, fn)
    if butil.fileExists(modFilePan):
        prn("**** File <{}> exists, aborting ****", modFilePan)
        return
    
    makeModFile(co, cocap, wash, vers, modFilePan)
    makeModDir(fnStub)

def makeModFile(co: str, cocap: str, 
                wash: bool, vers: bool,
                modFilePan: str):
    """ make the .md file for the mod """
    w = ("w" if wash else "")
    v = ("v" if vers else "")
    washVersStr = w + v
    if washVersStr:
        washVersStr = "_" + washVersStr
    cowv = co + washVersStr  
    washNot = (" " if wash else "not ")
    versNot = (" " if vers else "not ")
    
    TREATY_STRS = {
        "":    "No treaties",    
        "_w": "Washington Treaty",    
        "_v": "Versailles Treaty",    
        "_wv": "Washington+Versailles Treaties",           
    } 
    wPlusV = TREATY_STRS[washVersStr]
    modFileData = form(MOD_FILE_TEMPLATE,
        cowv = cowv,
        cocap = cocap,
        wPlusV = wPlusV,
        washNot = washNot,
        versNot = versNot,
    )    
    prn("Writing <{}>...", modFilePan)
    butil.writeFile(modFilePan, modFileData)
   
def makeModDir(fnStub):
    """ make the top directory of the mod """
    modDir = butil.join(MODS_DIR, fnStub, "Save")
    prn("Creating dir <{}/>...", modDir)
    butil.createDir(modDir)
    
    

#---------------------------------------------------------------------


def main():
    prn("mk1922mods = make mods for 1922 start")
    for co, cocap in COUNTRIES:
        for wash in [False, True]:
            for vers in [False, True]:
                makeMod(co, cocap, wash, vers)
            #//for vers
        #//for wash
    #//for co, cocap
    

if __name__=='__main__':
    main()

#end