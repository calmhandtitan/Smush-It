import mimetypes, urllib2, requests, os


class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'
        

# Class that validates a given url as an image
class ImageValidator:

	url = None
	valid_types = ('image/png', 'image/jpeg', 'image/gif', 'image/jpg')	
	
	def __init__(self):
		pass

	def get_contenttype(self):
		try:
			response= urllib2.urlopen(HeadRequest(self.url))
			maintype= response.headers['Content-Type'].split(';')[0].lower()
			return maintype
		except urllib2.HTTPError as e:
			print(e)
			return None

	def get_mimetype(self):
		(mimetype, encoding) =  mimetypes.guess_type(self.url)
		return mimetype

	def get_extension_from_type(self, type_string):
		if type(type_string) == str or type(type_string) == unicode:
			temp = type_string.split('/')
		if len(temp) >= 2:
			return temp[1]
		elif len(temp) >= 1:
			return temp[0]
		else:
			return None

	def validate(self, _url):
		self.url = _url		
		content_type = self.get_contenttype()
		if content_type in self.valid_types:
			return self.get_extension_from_type(content_type)
		mimetypes = self.get_mimetype()
		if mimetypes in self.valid_types:
			return self.get_extension_from_type(mimetypes)
		return None

