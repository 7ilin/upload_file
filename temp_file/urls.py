from django.conf.urls import url
from temp_file import views


urlpatterns = [
    url(r'^$', views.upload_file, name='upload_file'),
    url(r'^file/(?P<pk>[0-9]+)/$', views.view_file, name='view_file'),
    url(r'^check/(?P<pk>[0-9]+)/$', views.check_file, name='check_file'),
]

