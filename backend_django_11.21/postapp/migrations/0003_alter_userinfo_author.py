# Generated by Django 3.2.16 on 2022-11-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='author',
            field=models.TextField(),
        ),
    ]
