import os

from tonpy import process_file

if __name__ == "__main__":
    for tlb_file in os.listdir("./src/tonpy/tlb_sources/"):
        if '.tlb' in tlb_file:
            process_file(f"./src/tonpy/tlb_sources/{tlb_file}", f"./src/tonpy/autogen/{tlb_file[:-4]}.py")
