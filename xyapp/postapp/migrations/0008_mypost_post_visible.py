# Generated by Django 3.2.16 on 2022-11-26 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0007_mypost_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='post_visible',
            field=models.CharField(default='NO', max_length=50),
        ),
    ]