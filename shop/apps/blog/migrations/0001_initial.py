# Generated by Django 4.1.4 on 2022-12-31 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('family', models.CharField(max_length=30)),
                ('sulg', models.SlugField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
