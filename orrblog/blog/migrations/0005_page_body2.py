# Generated by Django 2.1.3 on 2018-11-18 07:23

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181118_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body2',
            field=markdownx.models.MarkdownxField(default=''),
        ),
    ]
