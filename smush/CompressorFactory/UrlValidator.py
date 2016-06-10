import urlparse, urllib

class UrlValidator:
	
	url = None
	def __init__(self):
		pass

	def urlWithScheme(self, _url):
		parsed_url = urlparse.urlparse(_url)
		if parsed_url.scheme:
			return _url
		else:
			parsed_url = parsed_url._replace(**{"scheme": "http"})
			return parsed_url.geturl()

	def isUrl(self, _url):
		self.url = self.urlWithScheme(_url)
		try:
			urllib.urlopen(self.url)
			return True
		except IOError:
			return False

