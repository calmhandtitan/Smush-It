from django.shortcuts import render
from .models import Images, Document
from .forms import DocumentForm
import magic, os, uuid
from CompressorFactory.FileProcessor import FileProcessor
from CompressorFactory.ImageCompressor import ImageCompressor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
valid_type = ["xls", "xlsx", "csv", "txt"]
valid_image = ["jpeg", "jpg", "png"]
img_proc = ImageCompressor()
output_file = None

def index(request):
	all_images = Images.objects.all()
	context = {'all_images': all_images}
	return render(request, 'smush/index.html', context)


def upload(request):
	if request.method == 'POST':
		form = DocumentForm()
		context = {'option_type': request.POST['option_type'], 'form': form}
		return render(request, 'smush/upload.html', context)
	else:
		return render(request, 'smush/index.html')
	

def compress(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			
			output_file = process_file(newdoc)
			
		elif request.POST['image_url']:
			output_file = img_proc.compress(request.POST['image_url'], str(uuid.uuid4()), BASE_DIR + '/media/')
		
		output_file = output_file[len(BASE_DIR)+1:]
		return render(request, 'smush/compress.html' , {'output_file': output_file})
	else:		
		return render(request, 'smush/index.html')


def process_file(doc):
	extension = doc.extension()[1:].lower()

	# path of the file uploaded by user containing url's to images to be compressed
	filepath = BASE_DIR + doc.docfile.url
	# path of file to be give to user containing url's to comrpressed images
	output_filepath = BASE_DIR
	if extension in valid_type:
		output_file = FileProcessor(filepath, extension, output_filepath + '/media/').process()
		return output_file
	elif extension in valid_image:
		output_file = img_proc.compress_image(doc.docfile.url, output_filepath)
		return output_file
	else:
		print "wrong file uploaded"
	