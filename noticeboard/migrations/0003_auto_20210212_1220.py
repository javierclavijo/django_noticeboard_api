# Generated by Django 3.1.6 on 2021-02-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0002_auto_20210212_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='exp_date',
            field=models.DateTimeField(verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date published'),
        ),
    ]