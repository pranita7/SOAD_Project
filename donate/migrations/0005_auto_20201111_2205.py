# Generated by Django 3.0.3 on 2020-11-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20201111_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate_images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='donate_images/'),
        ),
    ]