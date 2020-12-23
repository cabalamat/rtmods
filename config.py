# config.py = configuaration data

import sys

import butil
from butil import dpr

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
