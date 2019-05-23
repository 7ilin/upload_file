from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views.static import serve
from temp_file.forms import UploadFileForm
from temp_file.models import UploadFile
from datetime import datetime, timedelta


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.author = request.user
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

