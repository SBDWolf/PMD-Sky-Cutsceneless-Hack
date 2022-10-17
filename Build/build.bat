@echo off

if [%1]==[] goto usage

python patch_us_wm_codes.py .\modified\EU.nds

if not exist .\patches\flips mkdir .\patches\flips
if not exist .\patches\xdelta mkdir .\patches\xdelta

SET xdeltaEUpath=.\patches\xdelta\PMD.Sky.Cutsceneless.v%1.EU.WMCodes.xdelta
SET xdeltaUSpath=.\patches\xdelta\PMD.Sky.Cutsceneless.v%1.US.WMCodes.xdelta
SET flipsEUpath=.\patches\flips\PMD.Sky.Cutsceneless.v%1.EU.WMCodes.bps
SET flipsUSpath=.\patches\flips\PMD.Sky.Cutsceneless.v%1.US.WMCodes.bps

.\patchers\xdelta -s .\vanilla\vanilla.nds .\modified\EU.nds %xdeltaEUpath%
.\patchers\xdelta -s .\vanilla\vanilla.nds .\modified\US.nds %xdeltaUSpath%

.\patchers\flips --create .\vanilla\vanilla.nds .\modified\EU.nds %flipsEUpath%
.\patchers\flips --create .\vanilla\vanilla.nds .\modified\US.nds %flipsUSpath%

goto :eof

:usage
@echo Usage: %0 {version_number}
@echo For example: %0 1.0 

