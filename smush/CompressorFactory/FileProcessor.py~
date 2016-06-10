import xlrd, xlwt
import csv, sys, os, uuid
from ImageCompressor import ImageCompressor
from UrlValidator import UrlValidator


class FileProcessor:

	filetype = None
	filepath = None
	output_filename = None
	output_filepath = None
	output_imagepath = None
	img_comp = None
	url_valid = None
	
	url_list = []

	def __init__(self, _filepath, _filetype, _output_filepath):
		
		self.filepath = _filepath
		self.filetype = _filetype
		self.output_filepath  = _output_filepath
		self.output_imagepath = _output_filepath

		self.output_filename = str(uuid.uuid4()) + "." + self.filetype
		self.output_filepath += "tmp_files/" + self.output_filename
		
		self.img_comp = ImageCompressor()
		self.url_valid = UrlValidator()
		
		
	def process(self):
		if self.filetype == 'txt':
			self.processTextFile()
		elif self.filetype == 'csv':
			self.processCsvFile()
		elif self.filetype == 'xls' or self.fileType == 'xlsx':
			self.processXlsFile()
		return self.output_filepath
		
		
	def processTextFile(self):
		with open(self.filepath, 'r') as f:
			self.url_list = f.read().split("\n")
		f.closed
		self.url_list = [x.strip() for x in self.url_list if self.url_valid.isUrl(x)]
		
		# open output file for writing links to compressed images
		f = open(self.output_filepath, 'w')
		for url in self.url_list:
			output_url = self.img_comp.compress(url, str(uuid.uuid4()), self.output_imagepath)
			f.write(output_url + "\n")
		f.close()
			


	def processCsvFile(self):
		fw = open(self.output_filepath, 'w')
		with open(self.filepath, 'rb') as f:
			reader = csv.reader(f)
			try:
				for row in reader:
					for element in row:
						if self.url_valid.isUrl(element):
							output_url = self.img_comp.compress(element, str(uuid.uuid4()), self.output_imagepath) 
							fw.write(output_url)
						else:
							fw.write(element)
						if element == row[-1]:
							fw.write("\n")
						else:
							fw.write(",")
			except csv.Error as e:
				sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
		f.closed
		fw.close()
		
	def processXlsFile(self):
		workbook = xlrd.open_workbook(self.filepath)
		worksheet = workbook.sheet_by_name('Sheet1')

		new_workbook = xlwt.Workbook()
		new_sheet = new_workbook.add_sheet('Sheet1')

		for row in range(0, 100):
			try:
				element = worksheet.cell(row, 0).value
				if element == xlrd.empty_cell.value:
					continue
				if self.url_valid.isUrl(element):
					output_url = self.img_comp.compress(element, str(uuid.uuid4()), self.output_imagepath)
					new_sheet.write(row, 0, output_url)
			except IndexError as e:
				pass

		new_workbook.save(self.output_filename)
