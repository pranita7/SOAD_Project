# Generated by Django 3.0.3 on 2020-11-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201103_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='total',
        ),
        migrations.AddField(
            model_name='post',
            name='total_like',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]