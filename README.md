# Smush-It
A django based webapp which takes url's to images, compresses the images and returns back url to the compressed image.

###Dependencies:

**webp:** To install on Debian/Ubuntu, run

> $ sudo apt-get install webp

And the remaining ones are listed in *requirements.txt*, to install them run

> $  pip install -r requirements.txt

###Supported FileFormats:

Currently the app suports following input file formats: 

.txt -> Each line in the text file should be a url. If not it will not be processed.
.xls -> A url should be in the first column of each row in "Sheet1". Max supported URL's = 100
.csv -> Url's can be anywhere in the file. No limit on number of url's
.jpg -> No limit on maxsize or max dimensions
.png -> No limit on maxsize or max dimensions
