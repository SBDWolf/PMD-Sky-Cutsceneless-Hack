import sys

#This script makes the WM system on the EU ROM of PMD Sky utilize US passwords. All that is needed to do is replace an array of bytes.
#This script is called from the command line as "patch_us_wm_codes.py {path_to_file}" and patches over a copy of the ROM called "US.nds"

if(len(sys.argv) != 2):
    print("Invalid number of parameters. Usage: patch_us_wm_codes.py {path_to_file}")
    quit()

try:    
    with open(sys.argv[1], "rb") as f:
        romcontents = f.read()
except IOError:
    print("Could not read the specified file.")
    quit()

eu_byteswap = b'\x0E\x04\x03\x18\x09\x1E\x0A\x20\x10\x21\x14\x00\x13\x16\x05\x12\x06\x01\x17\x1C\x07\x1B\x0D\x1F\x15\x1A\x02\x0B\x0C\x19\x0F\x08\x1D\x11'
us_byteswap = b'\x07\x1B\x0D\x1F\x15\x1A\x06\x01\x17\x1C\x09\x1E\x0A\x20\x10\x21\x0F\x08\x1D\x11\x14\x00\x13\x16\x05\x12\x0E\x04\x03\x18\x02\x0B\x0C\x19'
found_byteswap_offset = romcontents.find(eu_byteswap)
if found_byteswap_offset != -1:
    print("Found EU byteswap pattern at offset " + str(hex(found_byteswap_offset)) + ". Replacing...")
else:
    print("Couldn't find EU byteswap pattern. Exiting.")
    quit()
newbyteswap = romcontents.replace(eu_byteswap, us_byteswap)
try:
    with open(r".\modified\US.nds", "wb") as f:
        f.write(newbyteswap)
        print("Done.")
except IOError:
    print("Could not write the file.")
    quit()
