# Generated by Django 4.0 on 2022-01-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='courseNumber',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]