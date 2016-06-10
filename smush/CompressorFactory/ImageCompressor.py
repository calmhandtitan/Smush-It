from subprocess import call
#call(["jpegoptim", "-q",  "f.jpg"])
#call(["cwebp", "f.jpg", "-quiet", "-resize", "800", "600", "-o", "a.jpg"])

import requests, os
from ImageValidator import ImageValidator
from StringIO import StringIO
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ImageCompressor:
	
	url = None
	image_type = None
	image_path = None
	valid_types = ['jpeg', 'jpg', 'webp', 'png']
	image_name = None
	img = None

	def __init__(self):
		self.img = ImageValidator()

	def isImage(self):
		self.image_type = self.img.validate(self.url)
		if self.image_type in self.valid_types:
			return True
		return False

	def downloadImage(self):
		r = requests.get(self.url)
		i = Image.open(StringIO(r.content))
		self.image_name += "."+self.image_type
		self.image_path += "images/" + self.image_name
		i.save(self.image_path, self.image_type)

	# download image from _url, compresses and gives back path to compressed image
	
	def compress(self, _url, _image_name, _image_path):
		self.url = _url
		self.image_name = _image_name
		self.image_path = _image_path
		if self.isImage():
			self.downloadImage()
			call(["cwebp", self.image_path, "-quiet", "-o", self.image_path+".webp"])
			call(["rm", self.image_path])
			return self.image_path+".webp"
		else:
			print 'Invalid URL'
		
	# compresses a single picture and gives back path to single picture
	def compress_image(self, _image_name, _image_path):

		self.image_name = _image_name
		self.image_path = _image_path + self.image_name
		print self.image_name
		print self.image_path
		call(["cwebp", self.image_path, "-quiet", "-o", self.image_path+".webp"])
		call(["rm", self.image_path])
		return self.image_path+".webp"
