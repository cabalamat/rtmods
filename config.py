# config.py = configuaration data

import sys

import butil
from butil import dpr

#---------------------------------------------------------------------
# info about mods

MOD_INFO = [
   ("invasion_range", "Increased invasion ranges"),
   ("ai_ships", "Lots of AI ships including some very big ones"),
]

modInfo = dict((k,v) for k,v in MOD_INFO)

#---------------------------------------------------------------------

LINUX = 'linux' in sys.platform

MODS_DIR = butil.join(__file__, "../mods")

if LINUX:
    CLEAN_RTW_DIR = butil.normalisePath("~/cab/clean_rtw")
    MODDED_RTW_DIR = butil.normalisePath("~/cab/modded_rtw")
else:
    CLEAN_RTW_DIR = r"C:\cab\clean_rtw"
    MODDED_RTW_DIR = r"C:\cab\modded_rtw"
    

#---------------------------------------------------------------------


#end
