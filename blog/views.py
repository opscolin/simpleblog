from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models.functions import Extract


# Create your views here.
# 首页
def index(request):
	blogs  = Blog.objects.order_by('-created')
	if blogs:
		return render(request, 'blog/index.html', {"blogs": blogs})

# 博客详情页
def detail(request, blogid):
	blog = Blog.objects.get(id=blogid)
	tags = blog.tags.all()
	if blog:
		return render(request, 'blog/detail.html', {'blog': blog, 'tags':tags})

# 按年份归纳页面
def year_archive(request, year):
	try:
		post_year = Blog.objects.filter(created__year=str(year))
	except Blog.DoesNotExist:
		raise Http404
	return render(request, 'blog/archive.html', {'post_year': post_year, 'year': year})

# 按分类归纳页面
def category_archive(request, categroy):
	try:
		posts = Blog.objects.filter(categroy__name=categroy)
	except Blog.DoesNotExist:
		raise Http404
	return render(request, 'blog/archive_by_category.html', {'posts':posts, 'categroy': categroy})

# 默认归纳页面，按照年份
def archives(request):
	try:
		post_lists = Blog.objects.order_by('-created')
	except Blog.DoesNotExist:
		raise Http404
	return render(request, 'blog/archives.html', {'post_lists': post_lists})

# about page
def about(request):
	return render(request, 'blog/about.html')

# 项目展示页
def project(request):
	return render(request, 'blog/project.html')
