# Generated by Django 4.2 on 2023-04-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_asfeaturedon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Asfeaturedon',
        ),
    ]
