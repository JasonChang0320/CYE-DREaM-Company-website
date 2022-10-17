# Generated by Django 4.0.6 on 2022-10-16 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_nstc_project_nstc_project_en'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Experience_EN',
        ),
        migrations.DeleteModel(
            name='NSTC_project',
        ),
        migrations.DeleteModel(
            name='NSTC_project_EN',
        ),
        migrations.RemoveField(
            model_name='service_title',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='service_title_en',
            name='title2',
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(blank=True, max_length=600, verbose_name='內容'),
        ),
    ]