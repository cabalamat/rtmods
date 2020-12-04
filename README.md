# README.md for rtmods

**Rtmods** (for "Rule the mods") is a modification installer/manager for 
Rule the Waves 2.

## Background

[**Rule the Waves 2**](https://nwswargamingstore.net/shop/ols/products/nws-rule-the-waves-ii)
(RTW2) is a wargame by NWS. In it, you are the commander of a navy of one of the world 
powers between 1900-1955. You can design ships, then fight those ships against the fleets
of other naval powers.

Some people have written modifications for RTW2. These mods can be fiddly to 
install involving massy faffing about with files. Rtmods aims to streamline the 
process.

## Dependencies

Rtmods requires Python 3.8 or later, plus a copy of Rule the Waves 2.

## Installation

## How it works

## Use

You can get help information using the -h flag, e.g.:

```
> python rtmods.py -h
usage: rtmods.py [-h] [-v] [-l] [-i MOD] [--reset] [--add MOD]

*** Rule the Mods -- a mod manager for RTW2 ***

optional arguments:
  -h, --help          show this help message and exit
  -v, --verbose       Increase output verbosity
  -l, --list          List mods available
  -i MOD, --info MOD  Display info about a particular mod
  --reset             Reset modded_rtw from clean_rtw
  --add MOD           Add a mod to modded_rtw
```

To install some mods, first reset your modded_rtw:

    > python rtmods.py --reset
    
Then install all the mods you want to, one at a time:

    > python rtmods.py --add mod1
    > python rtmods.py --add mod2
    > python rtmods.py --add mod3
    
Then play the game by running the RTW executable in modded_rtw

/end/
