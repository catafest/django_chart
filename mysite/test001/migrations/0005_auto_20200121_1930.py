# Generated by Django 3.0.1 on 2020-01-21 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0004_author_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_book',
            new_name='author_name',
        ),
    ]