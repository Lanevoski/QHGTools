## RYAN AKERS
## LANEVOSKI.COM
## Look at the README for details
import struct, os, sys

ADDR_NUMFILES = 0x004
ADDR_OFFSET_LIST = 0x008
OFFSET_MULTIPLIER = 0x800

def main():
    filename = sys.argv[1]
    cpk = open(filename,"rb")

    ## How many files do we have?
    cpk.seek(ADDR_NUMFILES)
    numFiles = struct.unpack('i',cpk.read(4))[0] + 1

    ## Get list of addresses
    ## Last value is address of EOF, no data
    fileOffsets = []
    cpk.seek(ADDR_OFFSET_LIST)
    for i in range(numFiles):
        fileOffsets.append(struct.unpack('H',cpk.read(2))[0] * OFFSET_MULTIPLIER)

    ## Make dir if non existant
    dirname = filename.split(".")[0]
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    ## Make files
    cpk.seek(fileOffsets[0])
    for i in range(len(fileOffsets)-1):
        file = open(dirname + "\\" + str(i),"wb")

        size = fileOffsets[i+1]-fileOffsets[i]
        file.write(cpk.read(size))
        
        file.close()

    cpk.close()

if(__name__ == "__main__"):
    main()

