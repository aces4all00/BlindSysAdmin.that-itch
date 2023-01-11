import re
import time
import os

codetypes = ('python', 'powershell', 'csharp')
doctypes = ('comment', 'note', 'post', 'unclassified')

def formatname(thisname, substitute = "-"):
    match_pattern = r"[^A-Za-z0-9]"
    return re.sub(f"{substitute}$", "", re.sub(match_pattern, substitute, thisname.lower()))

def formattime(thetime = time.gmtime(), theformat = "%Y-%m-%d %H:%M:%S %z"):
    return time.strftime(theformat, thetime)

def getprojectpath():
    return os.path.realpath(os.path.dirname(os.path.dirname(__file__)))