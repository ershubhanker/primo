# Generated by Django 4.2 on 2023-04-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
    ]
