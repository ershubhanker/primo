# Generated by Django 4.2 on 2023-04-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_buttontext_btn_txt'),
    ]

    operations = [
        migrations.CreateModel(
            name='paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para', models.TextField()),
            ],
        ),
    ]