
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<blogid>[1-9]+)/$', views.detail, name='detail'),
	url(r'^about/$', views.about, name='about'),
	url(r'^project/$', views.project, name='project'),
	url(r'^archives/$', views.archives, name='archives'),
	url(r'^year/(?P<year>[0-9]{4})/$', views.year_archive, name='year_archive'),
	# url(r'^category/(?P<category>[a-zA-Z]+)/$', views.category_archive, name='categroy_archive'),
	url(r'^category/(?P<categroy>\w+\.?\w+)/$', views.category_archive, name='categroy_archive'),
	# url(r'^category/(?P<categroy_id>[0-9]+)/$', views.category_archive, name='categroy_archive'),
]


