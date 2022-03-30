import os
if (os.file.exists('Debugcfg.py')):
    import Debugcfg
    token = Debugcfg.token
else:
    token = "NONE"
prefix = "bb!"