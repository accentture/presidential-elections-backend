# Generated by Django 3.2.3 on 2021-05-25 14:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_candidate_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo'),
        ),
    ]
