import bsaprojecthelper
import time
import os

title = bsaprojecthelper.formatname("My name is jonny!")
datestamp = bsaprojecthelper.formattime(time.gmtime()).split(" ")[0]
filename = f"{datestamp}-{title}.md"
print(filename)

first = ('one', 'two')
second = ('three', 'four')
print((bsaprojecthelper.codetypes + bsaprojecthelper.doctypes))

print(bsaprojecthelper.getprojectpath())

class bsaproject:
    def __init__(self, title, thetime):
        self.title = title
        self.time = thetime
        self.projfolder = bsaprojecthelper.getprojectpath()