# Generated by Django 3.0.3 on 2020-11-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
