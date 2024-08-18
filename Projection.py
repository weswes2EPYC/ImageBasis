from sympy import *
import sympy
from PIL import Image
import NewImage
class ProjectedImage:
    def __init__(self, image):
        self.projection_subspace = self.askForSubspace()
        self.projection_matrix = self.getProjectionMatrix(self.projection_subspace)
        self.image = image.copy()
        self.width, self.height = image.size
        self.projectedImage = self.projectImage(self.projection_matrix, self.image)

    def projectImage(self, projectionMatrix, image):
        pix = image.load()
        total = self.width * self.height
        counter = 0
        for x in range(self.width):
            for y in range(self.height):
                counter += 1
                pixel = pix[x, y]
                vector = Matrix([pixel[0], pixel[1], pixel[2]])
                proj = projectionMatrix * vector
                pix[x, y] = (proj[0, 0], proj[1, 0], proj[2, 0])
                print(round((counter/total) * 100, 2), "%")
        return image

    def getProjectionMatrix (self, columnSpace):
        eigenvalues = (columnSpace.T * columnSpace).eigenvals()
        if not eigenvalues.get(0) == None:
            columnSpace = columnSpace.col(0)
            print("vectors not lin ind")
        return columnSpace * (columnSpace.T * columnSpace)**-1 * columnSpace.T


    def askForVector (self, number):
        response = input("Enter RGB values for your " + number + " color separated by commas, no spaces. ex 10,150,200\n").replace(" ", "").split(",")
        if response == ["0", "0", "0"]:
            print("don't enter zero vectors")
            return self.askForVector(number)
        if not len(response) == 3:
            print("Input must have three values separated by commas!")
            return self.askForVector(number)
        for part in response:
            if not part.isdigit():
                print("All inputs must be positive integers!")
                return self.askForVector(number)
            elif int(part) > 255:
                print("RGB values must be between 0 and 255!")
                return self.askForVector(number)
        return response

    def askForSubspace(self):
        vector2 = Matrix(self.askForVector("first"))
        vector1 = Matrix(self.askForVector("second"))

        subspaceBasis = Matrix()
        subspaceBasis = subspaceBasis.col_insert(0, vector1)
        subspaceBasis = subspaceBasis.col_insert(1, vector2)
        return subspaceBasis


while true:
    image = Image.open(r"tree.jpg")
    proj = ProjectedImage(image)
    proj.projectedImage.show()