# Generated by Django 2.0.2 on 2018-04-16 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=150)),
                ('album_title', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=150)),
                ('album_logo', models.FileField(max_length=550, upload_to='Image/album_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('image_title', models.CharField(max_length=250)),
                ('is_fav', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to='Image/images')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.Album')),
            ],
        ),
    ]
