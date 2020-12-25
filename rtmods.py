# rtmods.py

import argparse
from typing import Iterable, Dict, List, Tuple, Any
import shutil
import pathlib

import butil
from butil import pr, prn, dpr, join
import config
from config import (LINUX, 
    MODS_DIR, CLEAN_RTW_DIR, MODDED_RTW_DIR)

verbosity = 0
modInfo = {}

#---------------------------------------------------------------------
# utility functions

def sorted_kv(d: Dict)->List[Tuple[Any,Any]]: 
    result = []
    for k in sorted(d.keys()):
        v = d[k]
        result.append((k,v))
    return result    

def padRight(s: str, n: int) -> str:
    """ add spaces to the end of (s) until it is at least (n) chars long.
    Doesn't truncate (s). 
    """
    if len(s) >= n: return s
    return s + (" "*(n-len(s)))

def forceMakeDestDir(destFile: pathlib.Path):
    """ force the creation of all directories above the file (destFile).
    If the directories already exist, silently do nothing.
    """
    destDir = destFile.parent
    destDir.mkdir(parents=True, exist_ok=True)

def copyIntoTree(src: str, dst: str):
    """ Copy files from directory structure (src) into directory 
    structure (dst), creating directories and over-writing files 
    where necessary.
    """
    numFilesCopied = 0
    srcP = pathlib.Path(src)
    dstP = pathlib.Path(dst)
    #dpr("srcP=%r", srcP)
    srcFilesDirs = list(srcP.rglob("*"))
    
    srcFiles = [f for f in srcFilesDirs
                if butil.fileExists(str(f))]
    #dpr("srcFiles=%r", list(srcFiles))
    for srcFile in srcFiles:
        relPath = srcFile.relative_to(srcP)
        #dpr("relPath=%r", relPath)
        dstForFile = dstP / relPath
        #dpr("dstForFile=%r", dstForFile)
        if verbosity>=2:
            prn("Copying {} to {}...", str(srcFile), str(dstForFile))
        forceMakeDestDir(dstForFile)    
        shutil.copyfile(str(srcFile), str(dstForFile))
        numFilesCopied += 1
    #//for srcFile
    prn("Copied {} files.", numFilesCopied)
        

#---------------------------------------------------------------------

def isValidModName(mn: str) -> bool:
    """ Is (mn) a valid module name? Valid mod names:
    * are 1-32 chars long
    * contain only lower case letters (a-z), digits (0-9) and the 
      underline ("_") char 
    """
    if len(mn)<1: return False
    if len(mn)>32: return False
    for ch in mn:
        if ch not in "abcdefghijklmnopqrstuvwxyz0123456789_":
            return False
    return True    

def getModNames() -> List[str]:
    """ Return all the valid mod names """  
    modsP = pathlib.Path(MODS_DIR)
    modDocs = modsP.glob("*.md") # mod documentation files
    #dpr("modDocs=%r", modDocs)
    modNames = []
    for modDoc in modDocs:
        modName = modDoc.stem
        #dpr("modName=%r", modName)
        if not isValidModName(modName):
            prn("mod name '{}' is invalid", modName)
            continue
        modDir = modsP / modName
        modDirStr = str(modDir)
        #dpr("modDir=%r modDirStr=%r", modDir, modDirStr)
        ex = butil.dirExists(modDirStr)
        #dpr("directory exists? ex=%r", ex) 
        if ex: modNames += [modName]
    #//for modDoc  
    return modNames

def getModDesc(modName: str) -> str:
    """ Get the description of a mod from its name. The description
    comes from the first line of the mod's documentation file.
    """
    modFnP = pathlib.Path(MODS_DIR) / (modName+".md")
    modFn = str(modFnP)
    modDoc = butil.readFile(modFn)
    line1 = modDoc.splitlines()[0]
    s = line1[1:].strip()
    if s.startswith(modName):
        s = s[len(modName):].strip()
    return s
    
def makeModList(): 
    """ creates the value of (modInfo) based on contents of the mod/ 
    directory.
    
    Every mod must have a {MOD}.md file and a {MOD}/ directory, where
    "{MOD}" must be the name of the mod. Mod names:
    
    * are 1-32 chars long
    * contain only lower case letters (a-z), digits (0-9) and the 
      underline ("_") char
    """   
    global modInfo
    modNames = getModNames()
    #dpr("modNames=%r", modNames)
    modInfo = dict((modName, getModDesc(modName)) 
                   for modName in modNames)
    #dpr("modInfo=%r", modInfo)

#---------------------------------------------------------------------
# commands from command line

def listMods():
    """ list mods avaialble """
    prn("List of all the mods...")
    for k,v in sorted_kv(modInfo):
        prn("{} {}", padRight(k,15), v) 
    #//for    
    
def infoMod(m: str):
    """ print information about mod (m) """
    if m in modInfo:
        description = modInfo[m]
        prn("Information on modification: {}\n{}", m, description)
    else:
        prn("There is no mod '{}'", m)

def resetModdedRtw():
    """ Reset modded_rtw from clean_rtw """
    
    #>>>>> first remove the existing modded_rtw
    try:
        prn("Removing existing {}...", MODDED_RTW_DIR)
        shutil.rmtree(MODDED_RTW_DIR)
    except Exception as ex:
        prn("On removal of {}, exception:\n{}", MODDED_RTW_DIR, ex)
        
    #>>>>> now we can copy clean_rtw into modded_rtw:
    prn("Resetting RTW; copying {} to {} ...",
        CLEAN_RTW_DIR, 
        MODDED_RTW_DIR)
    shutil.copytree(CLEAN_RTW_DIR, MODDED_RTW_DIR)
    prn("Finished!")
    

def addMod(m: str):
    """ Add mod (m) to the modded_rtw """
    if m not in modInfo:
        prn("There is no mod '{}'", m)
        return
    
    modDir = butil.join(MODS_DIR, m)
    if not butil.dirExists(modDir):
        prn("ERROR: Mod directory {} does not exist, aborting", modDir) 
    
    copyIntoTree(modDir, MODDED_RTW_DIR)
    prn("Mod {} installed!", m)
    

#---------------------------------------------------------------------

def main():
    global verbosity
    
    makeModList()
    
    parser = argparse.ArgumentParser(description=
        "*** Rule the Mods -- a mod manager for RTW2 ***")
    parser.add_argument("-v", "--verbose", action="count",
        help="Increase output verbosity")
    parser.add_argument("-l", "--list", action='store_true',
        help="List mods available")
    parser.add_argument("-i", "--info", type=str, metavar="MOD",
        help="Display info about a particular mod")
    parser.add_argument("--reset", action='store_true',
        help="Reset modded_rtw from clean_rtw (may take some time)")
    parser.add_argument("--add", type=str, metavar="MOD",
        help="Add a mod to modded_rtw")
    
    args = parser.parse_args()
    
    if args.verbose:
        verbosity = args.verbose
        prn("Verbosity={}", args.verbose)
        prn("MODS_DIR:       {}", MODS_DIR)
        prn("CLEAN_RTW_DIR:  {}", CLEAN_RTW_DIR)
        prn("MODDED_RTW_DIR: {}", MODDED_RTW_DIR)
        prn("LINUX?          {}", LINUX)
    else:
        verbosity = 0
    
    if args.list:
        listMods()
    elif args.info:
        infoMod(args.info)
    elif args.reset:
        resetModdedRtw()
    elif args.add:
        addMod(args.add)
    else:
        prn("Hint: use -h to get help information")
        


if __name__=='__main__':
    main()

#end
