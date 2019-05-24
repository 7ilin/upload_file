from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from temp_file import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.upload_file, name='upload_file'),
    url(r'^file/(?P<pk>[0-9]+)/$', views.view_file, name='view_file'),
    url(r'^check/(?P<pk>[0-9]+)/$', views.check_file, name='check_file'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutFormView.as_view()),
    url(r'^all_files/$', views.all_files, name='all_files')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)