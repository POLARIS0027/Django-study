# Generated by Django 4.0.3 on 2022-03-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_album_owner_photo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='SorlPhoto/%Y', verbose_name='IMAGE'),
        ),
    ]
