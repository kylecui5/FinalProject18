import os
import json

class ImageAnalyzer:

    def getBaselineCoords(self, drawing):
        """Returns saved coordinates of the corresponding baseline drawing"""

        path = os.path.abspath('BaselineDrawings.txt')
        baselineFile = open(path, "r")
        allCoords = json.load(baselineFile)
