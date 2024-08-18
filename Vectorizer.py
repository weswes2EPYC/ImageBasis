from sympy import *
import sympy
sympy.init_printing()
from PIL import Image
import NewImage
import numpy as np

'''
Amatrix = Matrix([])
print(Amatrix)
Amatrix = Amatrix.col_insert(0, Matrix([0, 0]))
print(Amatrix)
'''

image = Image.open(r"stars.jpg")
testNewBasisImage = NewImage.NewBasisImage(image)
array = np.array(testNewBasisImage.newImageList, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.show('peepeepoopoo')