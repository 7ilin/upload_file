# Generated by Django 2.2.1 on 2019-05-23 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temp_file', '0010_auto_20190524_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
