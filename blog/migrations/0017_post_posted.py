# Generated by Django 3.0.3 on 2020-12-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted',
            field=models.BooleanField(default=False),
        ),
    ]
