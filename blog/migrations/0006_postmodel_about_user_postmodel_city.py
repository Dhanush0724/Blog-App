# Generated by Django 5.0.2 on 2024-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_postmodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='about_user',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='city',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
