# Generated by Django 2.2.4 on 2021-05-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0002_auto_20210525_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
