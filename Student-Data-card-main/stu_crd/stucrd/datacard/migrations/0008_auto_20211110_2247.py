# Generated by Django 3.2 on 2021-11-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacard', '0007_auto_20211110_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='deg',
        ),
        migrations.AddField(
            model_name='degree',
            name='deg',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.RemoveField(
            model_name='degree',
            name='exm',
        ),
        migrations.AddField(
            model_name='degree',
            name='exm',
            field=models.ManyToManyField(to='datacard.Exam'),
        ),
    ]
