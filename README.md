# Python-image
### What [the program](https://github.com/chichikow/Python-image/blob/master/c_line.py) does
The program opens the image from the file and prints its height and width.
### Сode explanation
In this program we use the Image module.The module also provides a number of functions, including the functions of loading images from files and creating new images.
>Image.open()

This function opens and identifies the image file. In our program we pass functions 
image file location:
          
    f_name = input() 
    img = Image.open(f_name)

 Get image size:
 
    img.size 
 
Displays this image:
 
     Image.show()
    

### Program output 

![](https://github.com/chichikow/Python-image/blob/master/output_program.PNG) There you can see program output.

At the command line, we open our python file and pass it the image location.

----------------------------------------------------------------------------------------------------------------------------------------
# UPDATED PROGRAM

[This](https://github.com/chichikow/Python-image/blob/master/upgrate.py) is updated program.

### What the programs does

the program opens the image from the file and prints its height and width. +the program counts the number of green pixels in the image.

### Code explanation

In our program we use a numpy library and some of its functions.

> numpy.asarray() - Convert the input to an array.

In our case, the input is an image. We get a three-dimensional array.

The first thing we can do is linear search with a counter:

    count = 0
    for y in range(img.height):
        for x in range(img.width):
            pix = img.getpixel((x,y))
            if pix == (0,255,0):
            count += 1
            
But this case is not effective. We spend a lot of time, so we can use a numpy function.









