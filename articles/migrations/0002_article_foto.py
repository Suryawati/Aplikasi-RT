# Generated by Django 2.2.7 on 2020-07-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='foto',
            field=models.ImageField(blank=True, upload_to='foto/'),
        ),
    ]
