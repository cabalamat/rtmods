# modlog.py

""" The modlog is a log of mudifications that have been added.

Because --reset wipes the state of the <modded_rtw/> directory,
whenever a --reset occurs, the exisitng log is wiped and replaced
by a new one starting with --reset. Thus, --reset will always be 
the first event of as log.

The log is stored in JSON format in the file <modlog.json>. 

Example of a log file when converted to Python object format:
[
    ["2020-10-26 11:30", "--reset", ""],
    ["2020-10-26 11:38", "--add", "roc"],
    ["2020-10-26 11:39", "--add", "invasion_range"],        
]
"""

from typing import List
import datetime
import json

import butil
from butil import pr, prn, dpr, join

ModLog = List[List[str]]

#---------------------------------------------------------------------
# external interface

def getModLog() -> ModLog:
    ml = readModLog()
    return ml    

def notifyReset():
    """ notify that we've executed a --reset """  
    ml = [
        [getTimeStamp(), "--reset", ""],    
    ]
    writeModLog(ml)
    
def notifyAdd(modName: str):
    """ notify that we've added a mod """
    ml = readModLog()
    newAction = [getTimeStamp(), "--add", modName]
    ml.append(newAction)
    writeModLog(ml)

#---------------------------------------------------------------------
# lower level functions

MODLOG_PN = butil.join(__file__, "../modlog/modlog.json")
#prn("MODLOG_PN=%s", MODLOG_PN)


def getTimeStamp() -> str:
    """ return the current time in the format 'yyyy-mm-dd HH:MM' """
    dt = datetime.datetime.now()
    dtStr = dt.strftime("%Y-%m-%d %H:%M")
    return dtStr

def writeModLog(ml: ModLog):
    """ write (ml) to the modlog file """
    mlStr = json.dumps(ml, ensure_ascii=True, indent=4)
    butil.writeFile(MODLOG_PN, mlStr)
    
    
def readModLog() -> ModLog:
    """ read the modlog file """
    if butil.fileExists(MODLOG_PN):
        mlStr = butil.readFile(MODLOG_PN)
        ml = json.loads(mlStr)
        return ml
    else:
        prn("Mod log file <%s> doe not exist.", MODLOG_PN)
        return []
    


#end
