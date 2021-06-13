#!/usr/bin/env python

import sys
from plantuml import PlantUML

baseurl = 'http://www.plantuml.com/plantuml'
diagramExt = '.puml'

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "r") as file:
            self.file = file.read()
    
    def overwrite(self, contents):
        with open(self.filename, "w") as fileToWrite:
            fileToWrite.write(contents)

class DiagramHandler(FileHandler):
    def __init__(self, filename):
        FileHandler.__init__(self, filename)

    def generateUrl(self, url_prefix=baseurl, format="png"):
        pl = PlantUML(url=url_prefix+"/"+format+"/")
        return pl.get_url(self.file)

def main():
    if len(sys.argv) != 2:
        print("Need filename")
        return 1

    print(DiagramHandler(sys.argv[1]).generateUrl())
    return 0

if __name__== "__main__":
    main()
