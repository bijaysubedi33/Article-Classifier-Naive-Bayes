# Generated by Django 2.0.4 on 2018-05-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_auto_20180521_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='mypics/%Y/%m/%d'),
        ),
    ]
