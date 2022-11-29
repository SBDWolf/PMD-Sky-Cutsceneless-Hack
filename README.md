# PMD-Sky-Cutsceneless-Hack

A Hack of Pokémon Mystery Dungeon: Explorers of Sky that removes cutscenes while keeping gameplay as intact as possible.

Known issues:

- Some inconsistent music fades;
- The "Did you play "Explorers of Time" or "Explorers of Darkness" question is assumed to be answered as No. This is fine for every speedrunning category except for Recruit 'em All. A workaround should be to generate the save file on vanilla.

The source is just the files used by Skytemple.

Credits to reserve_cat from the PMD Speedruns Discord for the BAHAMUT Header Fix Patches.

---

To install:

- Acquire a clean European ROM of PMD Sky (note: roms labelled BAHAMUT need to have the BAHAMUT_Header_Fix patch applied first);
- Use Flips or xdelta to apply the patch of your choosing to the ROM.

If using Flips:

- Acquire a clean European ROM of PMD Sky;
- Acquire Flips from here: https://www.smwcentral.net/?a=details&id=11474&p=section ;
- Launch Flips and select Apply patch;
- Select the patch that you want to apply, then the ROM to apply that to (**make sure you are viewing all file types**), and then the name of the newly generated ROM file.

If using xdelta:

- Acquire a European ROM of PMD Sky;
- Use xdelta to apply the patch of your choosing to the ROM.

If using xdeltaUI, you might get weird error messages trying to apply these out of the box. This is caused by the version of xdeltaUI that you find online sometimes making use of an old version of the patcher. If you're having problem in trying to apply the patch, try following these steps:

- Delete xdelda.exe inside of the xdeltaUI folder;
- Go to this github link, then download the version of xdelta appropriate to your CPU architecture: https://github.com/jmacd/xdelta-gpl/releases/tag/v3.0.11 ;
- Take the executable file you just downloaded, put it inside the xdeldaUI folder and rename it to xdelta.exe;
- Run xdeltaUI and try applying the patch again.

--------

If you want to actually make use of the source code and/or the automatic patch maker:

The source included here only includes the changes made to the scripts. It does not include changes made to things like NPC placements and header data.
If you want to make use of the source to take a look at this hack in a complete sense, you should also apply the patches in the releases section, which contain those additional changes to the game data.

In the Build folder there is an environment to automatically create patches with flips and xdelta. To do so (on Windows):
- Place the modified ROM in the Build/modified folder and name it "EU.nds";
- Place the vanilla ROM in the Build/vanilla folder and name it "vanilla.nds";
- Download flips and xdelta and place them inside Build/patchers;
- Open a command prompt inside the Build folder and run build.bat {version_number}, where {version_number} is the version number for the hack (for example, build.bat 1.0). The resulting patches should be in Build/patches.
