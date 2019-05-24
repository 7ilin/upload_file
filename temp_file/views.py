from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.static import serve
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from temp_file.forms import UploadFileForm
from temp_file.models import UploadFile
from datetime import datetime, timedelta


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'temp_file/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'temp_file/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutFormView(TemplateView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            if request.user.is_authenticated:
                instance.author = request.user
            instance.save()
            url = request.build_absolute_uri(reverse('view_file', kwargs={'pk': instance.id}))
            return render(request, 'temp_file/file_url.html', {'url': url, 'pk': instance.id})
    else:
        form = UploadFileForm(initial={'finish_date': datetime.now()+timedelta(seconds=3600)})
    return render(request, 'temp_file/upload.html', {'form': form})


def view_file(request, pk):
    temp_file = get_object_or_404(UploadFile, pk=pk)
    if temp_file.is_outdated():
        raise Http404('Файл удален по истечению срока действия.')
    return serve(request, temp_file.upload.path, document_root='/', show_indexes=False)


def check_file(request, pk):
    temp_file = get_object_or_404(UploadFile, pk=pk)
    if temp_file.is_outdated():
        raise Http404('Файл удален по истечению срока действия.')
    return render(request, 'temp_file/check_file.html', {'temp_file': temp_file, 'pk': pk})


def all_files(request):
    all_file = UploadFile.objects.filter(author=request.user)
    return render(request, 'temp_file/all_files.html', {'all_file': all_file})


