# Generated by Django 5.0.2 on 2024-05-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postmodel_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='savecontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(blank=True, default='media\\default.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
