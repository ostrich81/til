# Generated by Django 3.2.7 on 2021-09-03 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='updated_ate',
            new_name='updated_at',
        ),
    ]
