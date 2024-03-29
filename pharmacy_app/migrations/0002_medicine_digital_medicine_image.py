# Generated by Django 4.2 on 2023-12-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
