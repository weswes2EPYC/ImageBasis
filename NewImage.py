from sympy import *
import sympy
sympy.init_printing()

class NewBasisImage:
    # constructor for a NewBasisImage, Image represented through a different basis
    def __init__(self, image):
        self.image = image  # the original image
        self.width, self.height = image.size  # the image's dimensions
        self.StandardVectors = self.vectorize(image)
        print("Finished vectorizing original image")
        self.BasisMatrix = self.findBasis(self.StandardVectors)  # the basis that forms the pixels
        print("Finished finding new Basis vectors")
        self.newImageList = self.newVectorized(self.BasisMatrix, self.StandardVectors)  # matrix of pixels in terms of BasisMatrix
        print("Finished representing image in new basis")

    # vectorized the entire image to the standard basis (ARGB)
    def vectorize(self, image):
        width, height = image.size
        AllMatrix = Matrix()
        pixel = image.load()
        total = width * height
        counter = 0
        for x in range(width):
            for y in range(height):
                counter += 1
                pix = pixel[x, y]
                ARGBvector = Matrix([pix[0], pix[1], pix[2]])
                AllMatrix = AllMatrix.col_insert(AllMatrix.shape[1], ARGBvector)
                print(round((counter/total) * 100, 2), "% done with vectorizing")
        return AllMatrix

    # finds a new basis of the vectorized pixels using the column space
    def findBasis(self, standard):
        columnSpace = standard.columnspace()
        basis = Matrix()
        for i in range(len(columnSpace)):
            basis = basis.col_insert(i, columnSpace[i])
        return basis

    # vectorizes the image in terms of the new basis
    def newVectorized(self, basis, oldVectors):
        EtoB = basis**-1
        newPixels = EtoB * oldVectors
        newPixelsList = [[0 for i in range(self.width)] for j in range(self.height)]
        total = self.width * self.height
        counter = 0
        for x in range(self.width):
            for y in range(self.height):
                pixelVector = newPixels.col(counter)
                pixel = (pixelVector[0], pixelVector[1], pixelVector[2])
                newPixelsList[y][x] = pixel
                counter += 1
                print(round((counter / total) * 100, 2), "% done with representing in new basis")
        return newPixelsList