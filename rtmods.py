# rtmods.py

import argparse
from typing import Iterable, Dict, List, Tuple, Any
import shutil
import pathlib

import butil
from butil import pr, prn, dpr
import config
from config import (modInfo, LINUX, 
    MODS_DIR, CLEAN_RTW_DIR, MODDED_RTW_DIR)

verbosity = 0

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
    srcP = pathlib.Path(src)
    dstP = pathlib.Path(dst)
    dpr("srcP=%r", srcP)
    srcFilesDirs = list(srcP.rglob("*"))
    dpr("srcFilesDirs=%r", srcFilesDirs)
    for fd in srcFilesDirs:
        dpr("fd=%r", fd)
        dpr("fd2=%r", str(fd))
    #//for    
    
    srcFiles = [f for f in srcFilesDirs
                if butil.fileExists(str(f))]
    dpr("srcFiles=%r", list(srcFiles))
    for srcFile in srcFiles:
        relPath = srcFile.relative_to(srcP)
        dpr("relPath=%r", relPath)
        dstForFile = dstP / relPath
        dpr("dstForFile=%r", dstForFile)
        if verbosity>=2:
            prn("Copying {} to {}...", str(srcFile), str(dstForFile))
        forceMakeDestDir(dstForFile)    
        shutil.copyfile(str(srcFile), str(dstForFile))
    #//for srcFile    
        

#---------------------------------------------------------------------

def listMods():
    """ list mods avaialble """
    prn("List of all the mods...")
    for k,v in sorted_kv(config.modInfo):
        prn("{}= {}", padRight(k,15), v) 
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
    prn("Finished.")
    

def addMod(m: str):
    """ Add mod (m) to the modded_rtw """
    if m not in modInfo:
        prn("There is no mod '{}'", m)
        return
        
    prn("!!!! TODO: adding mod {}", m)    
    
    modDir = butil.join(MODS_DIR, m)
    if not butil.dirExists(modDir):
        prn("ERROR: Mod directory {} does not exist, aborting", modDir) 
    
    copyIntoTree(modDir, MODDED_RTW_DIR)
    

#---------------------------------------------------------------------

def main():
    global verbosity
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
