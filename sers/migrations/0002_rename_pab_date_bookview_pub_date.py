# Generated by Django 4.1.2 on 2022-10-19 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookview',
            old_name='pab_date',
            new_name='pub_date',
        ),
    ]
