# Generated by Django 4.0.6 on 2022-08-15 07:12

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='標題')),
                ('content', models.TextField(blank=True, max_length=200, verbose_name='內容')),
                ('pic_url', models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='Service/experience_image', verbose_name='照片')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='標題')),
                ('content', models.TextField(blank=True, max_length=200, verbose_name='內容')),
                ('pic_url', models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='Service/service_image', verbose_name='照片')),
            ],
        ),
    ]