# Generated by Django 2.2.4 on 2019-08-27 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glovo', '0003_auto_20190820_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glovodeliverypermission',
            old_name='enabled',
            new_name='glovo_enabled',
        ),
    ]
