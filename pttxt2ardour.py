#!/usr/bin/env python

import sys

class PtTrack:

    
    
    def __init__(self):
        return
    def addRegion(self, 

class PtFileReader:

    _files = {}
    _regions = {}
    _tracks = {}

    _section = PtFileSection.HEADER

    def __init__(self, filename):
        self.filename = filename
        
        textFile = file(self.filename)
        self._parse_header(textFile)
        self._parse_file_definitions(textFile)
        self._parse_region_definitions(textFile)

    def _parse_header(self, textFile):
        """
        Parse the header section of a ProTools text file,
        which is a noop for now.
        """

        while 1:
            line = textFile.readline()
            if line ==  "F I L E S  I N  S E S S I O N\n":
                break
               
    def _parse_file_definitions(self, textFile):
        """
        Parse a the files section of a ProTools text file, whose lines
        have the format <filename> <tab> <path with : instead of / >,
        and add it to our map of filenames.
        """

        # Ignore the header line
        textFile.readline()

        while 1:
            line = textFile.readline().replace('\n', '')

            # Catch the section-switching line
            if line == "R E G I O N S  I N  S E S S I O N":
                break
            elif line != "":
                print "Files line:     " + line
                elements = line.split('\t')
                filename = elements[0]
                path = '/' + elements[1].replace(':', '/') + filename
                self._files[filename] = path

    def _parse_region_definitions(self, textFile):
        """
        Parse the regions section of a ProTools text file, whose lines
        have the format <region> <tab> <filename>, and add it to our map 
        of regions.
        """
        
        # Ignore the header line
        textFile.readline()

        while 1:
            line = textFile.readline().replace('\n', '')            

            # Catch the section-switching line
            if line == "T R A C K  L I S T I N G":
                break        
            elif line != "":
                elements = line.split('\t')
                region = elements[0]
                filename = elements[1]
                self._regions[region] = filename

    def _parse_track_definitions(self, textFile):
        """
        Parse the tracks section of a ProTools text file.
        """
        

    def _parse_single_track(self, textFile):
        
        

if __name__ == '__main__':
    reader = PtFileReader(sys.argv[1])
