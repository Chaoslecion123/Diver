# Generated by Django 2.2.4 on 2019-08-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0072_orderextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='language_code',
            field=models.CharField(default='es', max_length=35),
        ),
    ]
