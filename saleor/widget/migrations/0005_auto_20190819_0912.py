# Generated by Django 2.2.4 on 2019-08-19 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0004_benefit_benefittranslation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefit',
            options={'permissions': (('manage_benefits', 'Administrar beneficios.'),)},
        ),
    ]