# Generated by Django 2.2.3 on 2019-07-16 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='movie',
        ),
    ]
