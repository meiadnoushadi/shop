# Generated by Django 4.1.4 on 2022-12-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auther',
            name='image_name',
            field=models.CharField(default='nophoto.jpg', max_length=200),
        ),
    ]
