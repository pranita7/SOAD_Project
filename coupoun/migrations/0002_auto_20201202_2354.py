# Generated by Django 3.0.5 on 2020-12-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupoun', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gencode',
            name='codee',
            field=models.CharField(default='OERIP', max_length=5),
        ),
        migrations.AddField(
            model_name='gencode',
            name='codeee',
            field=models.CharField(default='OERIPLO', max_length=7),
        ),
        migrations.AlterField(
            model_name='gencode',
            name='code',
            field=models.CharField(default='OER', max_length=3),
        ),
    ]
