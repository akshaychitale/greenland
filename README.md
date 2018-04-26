# Greenland Flag Generator

A Python script to convert an image of a flag (or really any image) into one in the style of the flag of Greenland.

Made by **Akshay Chitale** for [/r/vexillology](https://www.reddit.com/r/vexillology/) on Reddit.

## How to Use

### Prerequisites

In order to run the Python script, you will, of course, have to have Python installed. The scripts was tested on macOS with both Python 2.7.13 and Python 3.6.4, so either Python 3 or Python 2.7 should work fine.

In addition, you will need to have the Python Imaging Library (PIL) installed. This can be installed with pip (or with pip3):

```
$ pip install Pillow
```

### Running the Script

Download the file `greenland.py` and run it with Python, passing in the name of the file to process:

```
$ python greenland.py image_in.png
```

For information about all of the options availible, such as setting the output image size, use the help option:

```
$ python greenland.py -h
usage: greenland.py [-h] [-s SIZE SIZE] [-n NAME] [-e EXT] [-d] [-v] image_in

positional arguments:
  image_in              Image file to process

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE SIZE, --size SIZE SIZE
                        Output image width and height
  -n NAME, --name NAME  Output file name
  -e EXT, --ext EXT     Output file extension
  -d, --display         Display output instead of saving to file
  -v, --verbose         Display progress while processing
```

### Advanced Use

You can also write your own script and just import the Greenland class to do more complicated things than the main script allows for. The Greenland class has the following methods:

* \_\_init\_\_ - Creates a new Greenland object
* greenland - Performs the Greenland flag transformation
* save - Saves the output image to a file
* show - Displays the output image in the default image viewer

Run `python greenland.py -h` to see what the arguments to the functions do. The main script just passes the command line arguments to these arguments in the Seychelles class's methods.

Feel free to modify any of the code, like the angle mapping or the algorithm itself, to make your own flag generators!

## Technical Details

The transformation that is performed is the 180 degree rotation of the circle in the middle left of Greenland's flag.  

The flag dimensions are described by [the Nordic Council](http://www.norden.org/en/fakta-om-norden-1/the-nordic-flags/the-greenland-flag). This circle is a circle centered at 7/18 the width of the flag and 1/2 the height of the flag. The radius of the circle is 1/3 the height of the flag if the flag is wider than a 2:3 aspect ratio, and is 2/9 the width of the flag if the flag is narrower than a 2:3 aspect ratio. Note that the flag of Greenland has a 2:3 aspect ratio. The calculated center has 1 pixel added to the height and width to account for rounding error.

The points within the circle are rotated 180 degrees about the center. This is equivalent to a reflection across each the vertical and horizontal through the center.
