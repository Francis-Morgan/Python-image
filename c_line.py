from PIL import Image

f_name = input() 
img = Image.open(f_name)
size = img.size
print('Размер изображения: ',size)
Image.open(f_name).show()

