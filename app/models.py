from django.db import models
from django.utils import timezone

from django.urls import reverse

class Comment(models.Model):
	name = models.CharField(max_length=20)
	comment = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)

class Review(models.Model):
	moviereview = models.TextField('review', null=True)
	sentiment = models.IntegerField(default=0)
	date = models.DateTimeField('create time', auto_now_add=timezone.now)

class ImageUpload(models.Model):
	image = models.ImageField(upload_to='upload_image/',
		null=True,
		blank=True,
		width_field='width_field',
		height_field='height_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

def upload_location(instance, filename):
	return '%s/%s' %(instance.id, filename)

class Article(models.Model):

	# STATUS_CHOICES = (
	# 	('u', 'unfinished'),
	# 	('p', 'published'),
	# 	)

	title = models.CharField('title', max_length=50)
	content = models.TextField('content', null=True)
	# image = models.FileField(null=True, blank=True)
	image = models.ImageField(upload_to=upload_location,
		null=True, 
		blank=True, 
		width_field='width_field',
		height_field='height_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	# part1 = models.TextField('part1', null=True)
	# img1 = models.FileField('file1', null=True, blank=True, upload_to='documents/%Y/%m/%d/')
	# part2 = models.TextField('part2', null=True, blank=True)
	# img2 = models.FileField('file2', null=True, blank=True, upload_to='documents/%Y/%m/%d/')
	# part3 = models.TextField('part3', null=True, blank=True)
	# img3 = models.FileField('file3', null=True, blank=True, upload_to='documents/%Y/%m/%d/')


	published_time = models.DateTimeField('create time', auto_now_add=timezone.now)
	last_modified_time = models.DateTimeField('last modified time', auto_now=True)

	# status = models.CharField('status', max_length=1, choices=STATUS_CHOICES)

	# views = models.PositiveIntegerField('views time')

	# put_on_top = models.BooleanField('top')

	abstract = models.CharField('abstract', max_length=20, blank=True,
		help_text='null is enabled')

	# category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

	class Meta:

		ordering = ['-last_modified_time']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={'pk':self.id})


class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField('Category name', max_length=20)
	create_time = models.DateTimeField('Create time', auto_now_add=True)
	last_modified_time = models.DateTimeField('Last modeified time', auto_now=True)

	def __str__(self):
		return self.name
		


