# firepower_etc = increased gun firepower

* By: cabalamat
* Added to Rtmods by: cabalamat
* Version: 0.1
* Date: 2025-Jul-23
* Date added to Rtmods: 2025-Jul-23

The **firepower_etc** mod replaces my earlier **invasion_range** mod.

It does three things:

* increases rate of fire in guns
* increases accuracy of gunfire, espcially in the early game
* increases invasion range

Increasing ROF and accuracy is to make make gunfire more useful because
in the early game (before c. 1910) it is ineffective which means lots of
small ships armed with torpedoes win.

I have added invasion range to the ifmod as it is also affects the same
file (`ResearchAreas2.dat`).

### Increased rate of fire

This is determined by `Gundata.dat`. ROF is the number of rounds that can
be fired in 8 minutes and the game has a limit of 4 rounds/min.

Calibre | Original | New
------- | -------- | ---
 2      |  25      |  45
 3      |  25      |  40
 4      |  20      |  36
 5      |  19      |  34
 6      |  18      |  32
 7      |  16      |  28
 8      |  15      |  24
 9      |  14      |  22
10      |  12      |  20
11      |  11      |  19
12      |  10      |  18
13      |   9      |  17
14      |   9      |  16
15      |   8      |  16
16      |   8      |  15
17      |   8      |  15
18      |   8      |  14
19      |   7      |  14
20      |   7      |  13

### Accuracy

This is deterrmined in `ResearchAreas2.dat` in the `[Fire control 3]`
section. I have moved some of the years forward:

Advance                     | Original | New
--------------------------- | -------- | ------
Coincidence rangefinder     |  1900    | 1900
6 ft rangefinder            |  1902    | 1900
Central firing              |  1903    | 1901
Range calculator            |  1903    | 1901
Control tops                |  1904    | 1902
Automatic range transmitter |  1905    | 1902
9 ft rangfinder             |  1905    | 1903
Mechanical fire control com |  1905    | 1903
Stereoscopic rangefinder    |  1906    | 1904
Plotting table              |  1908    | 1906
Target designator           |  1911    | 1908
Director firing             |  1912    | 1909
12 ft rangefinder           |  1912    | 1910
Ladder shooting             |  1912    | 1911

### Invasion Range

This increases the ranges at which invasions are possible. The purpose
is to make invasions easier.

It does this by altering the due-dates for technologies in Amphibious
Operations, in the file `ResearchAreas2.dat`.

Here is a list of the data of each advance in the original and new
`ResearchAreas2.dat` files:

Advance                     | Original | New
--------------------------- | -------- | ------
X-Lighters                  |  1908    |  1902
Elpidifor boats             |  1910    |  1903
Daihatsu barges             |  1912    |  1904
Motor Landing Craft         |  1914    |  1905
Amphibious tractors         |  1916    |  1906
Combat supply loading       |  1918    |  1907
Higgins boats               |  1920    |  1908
Assault landing craft       |  1922    |  1909
Specialized landing craft   |  1924    |  1910
