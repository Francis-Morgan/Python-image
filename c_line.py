from PIL import Image
import os


f_name = input() 
img = Image.open(f_name)
size = img.size
print('Размер изображения: ',size)
Image.open(f_name).show()

