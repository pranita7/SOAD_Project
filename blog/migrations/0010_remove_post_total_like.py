# Generated by Django 3.0.3 on 2020-11-02 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_total_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='total_like',
        ),
    ]
