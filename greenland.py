from __future__ import print_function
from PIL import Image
import argparse
import math
import os

# By Akshay Chitale for r/vexillology on Reddit

# For Python 3
try:
	xrange
except NameError:
	xrange = range

class Greenland:
	def __init__(self, name_in, size_out=None, name_out=None, ext_out=None):
		# Set up input
		self.name_in, self.ext_in = os.path.splitext(name_in)
		self.img_raw = Image.open(name_in)
		self.img_raw = self.img_raw.convert('RGB')
		self.size_in = self.img_raw.size
		# Flip so that colors are measured from top left
		self.img_in = self.img_raw.transpose(Image.FLIP_TOP_BOTTOM)

		# Set up output
		self.size_out = size_out if size_out else self.size_in
		self.name_out = name_out if name_out else self.name_in + '_out'
		self.ext_out = '.' + ext_out if ext_out else self.ext_in
		self.img_out = Image.new('RGB', self.size_out)
		self.pixels_out = self.img_out.load()

		# Set up image to print
		self.img_print = None

	def _determine_circle(self, width, height):
		# Center 7/18 of the width, 1/2 of the height
		center = (7*(width-1)/18.0, (height-1)/2.0)
		# Based on aspect ratio compared to 2:3, determine radius
		if width > 3*height/2.0:
			radius = height/3.0
		else:
			radius = 2.0*width/9.0
		return radius, center

	def _rotate_point(self, point, radius, center):
		# Flip points across center if within circle
		if radius**2 >= (point[0] - center[0])**2 + (point[1] - center[1])**2:
			x = 2*center[0] - point[0]
			y = 2*center[1] - point[1]
			return x, y
		else:
			return point

	def greenland(self, verbose=False):
		# Determine input and output circles
		out_circle = self._determine_circle(*self.size_out)
		# Find output color for each output pixel
		if verbose:
			print(' Progress:   0%', end='\r')
		for x in xrange(self.size_out[0]):
			if verbose:
				print('\r Progress: ' + str(int(100*x/self.size_out[0])).rjust(3) + '%', end='\r')
			for y in xrange(self.size_out[1]):
				out_x, out_y = self._rotate_point((x,y), *out_circle)

				# Coordinates on the input are:
				# x = out_x, scaled by width of input/output
				in_x = out_x * 1.0 * self.size_in[0] / self.size_out[0]
				# y = out_y, scaled by height of input/output
				in_y = out_y * 1.0 * self.size_in[1] / self.size_out[1]

				# Ensure coordinates are within range
				in_x_int = int(round(in_x))
				if in_x_int < 0:
					in_x_int = 0
				elif in_x_int >= self.size_in[0]:
					in_x_int = self.size_in[0] - 1
				in_y_int = int(round(in_y))
				if in_y_int < 0:
					in_y_int = 0
				elif in_y_int >= self.size_in[1]:
					in_y_int = self.size_in[1] - 1

				# Assign input color to output color
				self.pixels_out[x,y] = self.img_in.getpixel((in_x_int, in_y_int))
		if verbose:
				print('\r Progress: 100%')
		# Flip so that greenland is from bottom left
		self.img_print = self.img_out.transpose(Image.FLIP_TOP_BOTTOM)

	def save(self, name_out=None, ext_out=None):
		if self.img_print is None: raise Exception('No processing done yet')
		name = name_out if name_out else self.name_out
		ext = '.' + ext_out if ext_out else self.ext_out
		self.img_print.save(name + ext)

	def show(self):
		if self.img_print is None: raise Exception('No processing done yet')
		self.img_print.show()	

if __name__ == "__main__":
	# Parse args
	parser = argparse.ArgumentParser()
	parser.add_argument('image_in', type=str, help='Image file to process')
	parser.add_argument('-s', '--size', type=int, nargs=2, default=None, help='Output image width and height')
	parser.add_argument('-n', '--name', type=str, default=None, help='Output file name')
	parser.add_argument('-e', '--ext', type=str, default=None, help='Output file extension')
	parser.add_argument('-d', '--display', action='store_true', default=False, help='Display output instead of saving to file')
	parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Display progress while processing')
	args = parser.parse_args()

	# Run Seychelles
	g = Greenland(args.image_in, size_out=args.size, name_out=args.name, ext_out=args.ext)
	g.greenland(verbose=args.verbose)
	if(args.display):
		g.show()
	else:
		g.save()

