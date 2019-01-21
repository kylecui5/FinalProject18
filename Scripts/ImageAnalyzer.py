import os
import math
import json

class ImageAnalyzer:
    """Provides image analyzer functions"""

    def getDistTwoPoints(self, pointOne, pointTwo):
        """Returns the distance between pointOne and pointTwo"""

        pointOneX = int(pointOne[1:-(len(pointOne) - pointOne.index(","))])
        pointOneY = int(pointOne[(2 + pointOne.index(",")): -1])
        pointTwoX = int(pointTwo[1:-(len(pointTwo) - pointTwo.index(","))])
        pointTwoY = int(pointTwo[(2 + pointTwo.index(",")): -1])

        xDist = abs(pointOneX - pointTwoX)
        yDist = abs(pointOneY - pointTwoY)

        return math.sqrt(xDist * xDist + yDist * yDist)
    
    def getClosestPoint(self, point, listOfPoints):
        """Returns the closest point in listOfPoints to point"""

        closestDist = 100000000000

        for n in range(self.getNumCoords(listOfPoints)):

            eachDist = self.getDistTwoPoints(point, listOfPoints.splitlines()[2 + n])

            if eachDist < closestDist:
                closestDist = eachDist
                closestPoint = listOfPoints.splitlines()[2 + n]
        
        return closestPoint

    def getMultiplyFactor(self, drawing, drawingsList):
        """Returns the multiply factor for eachDistance to balance
        drawings with more coordinates with drawings with less coordinates"""

        numCoordsDrawing = self.getNumCoords(drawing)

        maxNumCoordsDrawing = 0

        for n in range(len(drawingsList)):
            coordString = self.getBaselineCoords(drawingsList[n])
            if self.getNumCoords(coordString) > maxNumCoordsDrawing:
                maxNumCoordsDrawing = self.getNumCoords(coordString)
                maxDrawing = n
        
        maxCoordString = self.getBaselineCoords(drawingsList[maxDrawing])
        return numCoordsDrawing / self.getNumCoords(maxCoordString)

    def getNumCoords(self, coordString):
        """Returns the first line of coordString which is the number of coordinates in coordString"""

        return int(coordString.splitlines()[0])

    def getBaselineCoords(self, drawing):
        """Returns saved coordinates of the corresponding baseline drawing"""

        if drawing == "apple":
            path = os.path.abspath('Apple.txt')
        elif drawing == "baseball":
            path = os.path.abspath('Baseball.txt')
        elif drawing == "basketball":
            path = os.path.abspath('Basketball.txt')
        elif drawing == "bird":
            path = os.path.abspath('Bird.txt')
        elif drawing == "candle":
            path = os.path.abspath('Candle.txt')
        elif drawing == "clock":
            path = os.path.abspath('Clock.txt')
        elif drawing == "coffee mug":
            path = os.path.abspath('CoffeeMug.txt')
        elif drawing == "smiley face":
            path = os.path.abspath('SmileyFace.txt')

        baselineFile = open(path, "r")
        return json.load(baselineFile)

    def compareDrawings(self, userDrawing, drawings):
        """Compares userDrawing to each baseline drawing"""

        leastDistance = 1000000000000000000000000
        eachDistance = 0

        numCoordsUserDrawing = self.getNumCoords(userDrawing)
        
        for n in range(len(drawings)):
            baselineDrawingString = self.getBaselineCoords(drawings[n])
            numCoordsBaselineDrawing = self.getNumCoords(baselineDrawingString)

            if numCoordsUserDrawing < numCoordsBaselineDrawing:
                for i in range(numCoordsUserDrawing):
                    closestPoint = self.getClosestPoint(userDrawing.splitlines()[2 + i], baselineDrawingString)
                    eachDistance += self.getDistTwoPoints(userDrawing.splitlines()[2 + i], closestPoint)
                    totalDistance = eachDistance / numCoordsUserDrawing
            else:
                for i in range(numCoordsBaselineDrawing):
                    closestPoint = self.getClosestPoint(baselineDrawingString.splitlines()[2 + i], userDrawing)
                    eachDistance += self.getDistTwoPoints(baselineDrawingString.splitlines()[2 + i], closestPoint)
                    totalDistance = eachDistance / numCoordsBaselineDrawing + 3
            
            if numCoordsUserDrawing == numCoordsBaselineDrawing:
                totalDistance -= 3
            print(f"Distance to {drawings[n]} is: {totalDistance}")
            #totalDistance = eachDistance * self.getMultiplyFactor(baselineDrawingString, drawings)

            if totalDistance < leastDistance:
                leastDistance = totalDistance
                guessDrawing = drawings[n]

            eachDistance = 0

        return guessDrawing