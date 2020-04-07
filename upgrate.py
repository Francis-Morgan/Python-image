from PIL import Image
import numpy as np
import sys

f_name = sys.argv[1] 
img = Image.open(f_name)
size = img.size
print('Image size: ',size)
arr = np.asarray(img)
print("Picture has ",np.count_nonzero((arr == [0,255,0]).all(axis = 2))," green pixels")






        

