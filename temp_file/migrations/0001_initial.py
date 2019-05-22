# Generated by Django 2.2.1 on 2019-05-18 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('upload', models.FileField(upload_to='uploads/', verbose_name='Загрузочный файл')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]