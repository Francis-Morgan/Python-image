# Python-image
### What [the program](https://github.com/chichikow/Python-image/blob/master/c_line.py) does
The program opens the image from the file and prints its height and width.
### Сode explanation
In this program we use the Image module from PIL (Python Image Library).The module also provides a number of functions, including the functions of loading images from files and creating new images.
>Image.open()

Besides, we'll need the sys module.The sys module provides access to some variables and functions that interact with the python interpreter.
>sys.argv

sys.argv is a list of command line arguments passed to the Python script. sys.argv[0] - this is the script name.

This function opens and identifies the image file. In our program we pass functions 
image file location:
          
    f_name = sys.argv[1] 
    img = Image.open(f_name)

 Get image size:
 
    img.size 
 
Displays this image:
 
     Image.show()
    

### Program output 

![](https://github.com/chichikow/Python-image/blob/master/output_program.PNG) 

There you can see program output.

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
            
But this case is not effective. We spend a lot of time, so we can use other method.

> numpy.count_nonzero() - counts the number of non-zero values in the array.

     np.count_nonzero(arr)

We get nonzero elements in the picture, but we need only green (0,255,0) elements.

> numpy.all() - Test whether all array elements along a given axis evaluate to True.

    np.count_nonzero((arr == [0,255,0]).all(axis = 2))

We check all array elements along the 2 axis have values (0.255.0). 
Axis 2, because we have three-dimensional array and we need check a value in pixel 

**OUTPUT**

input picture: 

![](https://github.com/chichikow/Python-image/blob/master/picture1.png)

output:

![](https://github.com/chichikow/Python-image/blob/master/output.PNG)










