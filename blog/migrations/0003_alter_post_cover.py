# Generated by Django 3.2.9 on 2022-04-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211130_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.CharField(max_length=255),
        ),
    ]
