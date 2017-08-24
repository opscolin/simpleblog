from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField('name', max_length=16)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField('name', max_length=16)

	# def __unicode__(self):
	def __str__(self):
		return self.name

class Blog(models.Model):
	title = models.CharField('title', max_length=32)
	author = models.CharField('author', max_length=16)
	abstract = models.TextField('abstract',default=None)
	content = models.TextField('content')
	# created = models.DateTimeField('pubdate', auto_now_add=True)
	created = models.DateField('pubdate', auto_now_add=True)

	categroy = models.ForeignKey(Category, verbose_name='category')
	tags = models.ManyToManyField(Tag, verbose_name='tag')

	def __str__(self):
		return self.title



class Experiment(models.Model):
    start_datetime = models.DateTimeField()
    start_date = models.DateField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
