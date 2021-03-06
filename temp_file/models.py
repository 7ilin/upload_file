from django.db import models
from django.utils import timezone


class UploadFile(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    upload = models.FileField(upload_to='uploads/', verbose_name='Загрузочный файл')
    created_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(null=False, verbose_name='Введите время действия файла')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def is_outdated(self):
        if self.finish_date:
            return timezone.now() > self.finish_date
