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

First install [Python](https://www.python.org/) 
and [Git](https://git-scm.com/) on your system.

Then create the directory `C:\cab\`. In this directory, use git to download Rtmods:

```
C:\cab> git clone git@github.com:cabalamat/rtmods.git
```

This downloads RTmods from Github into `C:\cab\rtmods`.

Now create a clean copy of Rule the Waves II into `C:\cab\clean_rtw\`.

That's it! Rtmods is now ready to run. 

## Directories and files used

* `C:\cab\rtmods\` = the top directory fo the Rtmods program
* `C:\cab\rtmods\rtmods.py` = the executable for the Rtmods program
* `C:\cab\rtmods\README.md` = this file you are now reading
* `C:\cab\rtmods\mods\` = Each mod goes under here in a separate directory hierarchy
* `C:\cab\clean_rtw\` = this is a clean copy of Rule the Waves II
* `C:\cab\modded_rtw\` = this is a copy of Rule the Waves II, with some mods added

For each mod there is a mod directory and a mod documatation file, for 
example the invasion-range mod has:

* `C:\cab\rtmods\mods\invasion_range.md` = the mod's documentation file
* `C:\cab\rtmods\mods\invasion_range\` = the mod directory

## How it works

There are essentially two operations that Rtmods can perform:

**Reset the modded_rtw**. The `--reset` command, which deletes `modded_rtw\` 
and copies `clean_rtw` over it. This makes `modded_rtw\` back into a pristine 
copy of the game.

**Add a mod**, usingf the `--add` command. After you have reset the `modded_rtw\`, 
you can then add mods to it one at a time. Adding a mod works by looksing at the 
mod's directory under `C:\cab\rtmods\mods\` and copying the files (asnd their 
directories) found there into `modded_rtw\`.

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
    
Then play the game by running the RTW executable in `C:\cab\modded_rtw\RTW2.exe`.

## Future enhancements

I might add a web-based interface for it, running on localhost.

This would list the mods available, display their descriptions and any instructions
for them. There would be hyperlinks to the mod's homepage, if any.

At the moment Rtmods doesn't remember what mods have been added to `modded_rtw\`.
This feature could be added, and then the program would be able to
display a log of what mods you have already added.

There will also be a short guide on how to write a mod and put it on the system.


/end/
