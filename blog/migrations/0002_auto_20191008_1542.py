# Generated by Django 2.2.6 on 2019-10-08 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tiele',
            new_name='title',
        ),
    ]
