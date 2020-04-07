from PIL import Image
import sys

f_name = sys.argv[1] 
img = Image.open(f_name)
size = img.size
print('Размер изображения: ',size)
Image.open(f_name).show()

