from django.conf.urls import url
from temp_file import views


urlpatterns = [
    url(r'^$', views.upload_file, name='upload_file'),
    url(r'^success$', views.success, name='success'),
    url(r'^file/(?P<pk>[0-9]+)/$', views.view_file, name='view_file'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

