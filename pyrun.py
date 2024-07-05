"""
------------------------------------
Coded by : @x_spoilt 
Uploaded by : @exotic_obfuscation
Github   : team-peaky-xd
------------------------------------


Features : 
- Detect Library's 
- Detect Installed Library's
- Install Library (Auto)
- Open-Source

Main-Feature : No ModuleNotFound Error ! 



"""
import subprocess as __0x1
import sys as __0x2
import os as __0x3
import importlib.util as __0x4

def __0x5(__0x6):
    __0x1.check_call([__0x2.executable, "-m", "pip", "install", __0x6])

def __0x7(__0x8):
    return __0x4.find_spec(__0x8) is not None

def __0x9(__0xA):
    with open(__0xA, 'r') as __0xB:
        __0xC = __0xB.readlines()
    
    __0xD = set()
    for __0xE in __0xC:
        __0xE = __0xE.strip()
        if __0xE.startswith('import '):
            __0xF = __0xE.split()[1].split('.')[0]
            __0xD.add(__0xF)
        elif __0xE.startswith('from '):
            __0xF = __0xE.split()[1].split('.')[0]
            __0xD.add(__0xF)
    
    __0x10 = __0x1.check_output([__0x2.executable, "-m", "pip", "freeze"]).decode("utf-8").split('\n')
    __0x10 = [__0x11.split('==')[0] for __0x11 in __0x10]

    for __0x12 in __0xD:
        if not __0x7(__0x12) and __0x12 not in __0x10:
            print(f"Installing {__0x12}...")
            __0x5(__0x12)

def __0x13(__0xA):
    __0x1.run([__0x2.executable, __0xA])

if __name__ == "__main__":
    if len(__0x2.argv) != 2:
        print("Usage: pyrun <script_path>")
        __0x2.exit(1)
    
    __0xA = __0x2.argv[1]
    
    if not __0x3.exists(__0xA):
        print(f"{__0xA} does not exist.")
        __0x2.exit(1)

    __0x9(__0xA)
    __0x13(__0xA)
