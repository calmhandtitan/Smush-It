from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
import os


class Images(models.Model):
	original_url = models.CharField(max_length=250)
	compressed_url = models.CharField(max_length=250)

	def __str__(self):
		return self.original_url + ' - ' + self.compressed_url

class Document(models.Model):
	docfile = models.FileField(upload_to='tmp_files')

	def extension(self):
		name, extension = os.path.splitext(self.docfile.name)
		return extension