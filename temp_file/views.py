from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from temp_file.forms import UploadFileForm
from temp_file.models import UploadFile
from pathlib import Path


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFile(upload=request.FILES['upload'])
            instance.save()
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'temp_file/upload.html', {'form': form})


def success(request):
    return HttpResponse('success')


def view_file(request, pk):
    temp_file = get_object_or_404(UploadFile, pk=pk)
    #import pdb; pdb.set_trace()
    fullpath = Path(temp_file.upload.path)
    # with open(temp_file.upload, 'rb') as s:
    #     data = s.read()
    if temp_file.is_outdated():
        raise Http404('Файл удален по истечению срока действия.')
    return FileResponse(fullpath.open('rb'), 'application/octet-stream')


