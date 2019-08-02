Starbound-Modding-Automation-Tools-WIP
============================
This is a set of tools to automate the modding process for Starbound. These tools allow you to patch hundreds or even thousands of files in the game. Included is a demo which will create patch food items to create "allergies".

WARNING:
============================
These tools make use of file IO. Be very careful when writing or deleting files otherwise you might create mass amounts of junk files or accidentally delete unintended files.

Requirements:
============================
- Python
- MongoDB
- pyMongo
- Starbound
- Starbound's Unpacked Assets


Helpful Tutorials/Links
============================
Installing MongoDB:
https://www.youtube.com/watch?v=Gum1XY52oFI

Getting MongoDB to work with Python:
https://www.youtube.com/watch?v=onuOSdOWcqQ

Unpacking Starbound Assets:
https://starbounder.org/Help:Unpacking_Game_Files

Video Demonstrating Allergy Maker usage:
https://www.youtube.com/watch?v=cVOwaLUGnOI


Main Tools:
============================
jacknife.py:
General use tools 

dalfileio.py:
Generic methods/data access layer for reading files and handling JSON.

dalmongo.py:
Some methods/data access layer for reading and handling MongoDB

sbmodio.py:
Makes use of dalfileio and dalmongo to create mods for Starbound

FilePlacementToGetThisToWork.png:
Shows you how the files should be arranged to get this mod to work

Allergy Demo:
============================
allergy.py:
The core file for creating allergy mods.

allergyWrangler.py
Provides automated methods for making pre-defined and custom allergies using allergy.py.

demo.py
The main entry point for the project. Executing this should provide an interface to run the demo.
