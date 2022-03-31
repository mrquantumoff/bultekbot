
from pathlib import Path
#import pathlib
debugcfg = Path("src/Debugcfg.py")
if (debugcfg.is_file()):
    import Debugcfg
    token = Debugcfg.token
    timeout = Debugcfg.timeout
    print("Debugcfg.py found, using token: " + token)
else:
    token = "NONE"
    timeout = 10
    if token == "NONE":
        print("Debugcfg.py not found, if you are sure that it exists please change working directory to the project root")
prefix = "bb!"