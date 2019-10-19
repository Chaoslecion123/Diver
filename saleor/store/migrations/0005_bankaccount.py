# Generated by Django 2.2 on 2019-04-20 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0023_auto_20190420_1827'),
        ('store', '0004_auto_20190417_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('bbva', 'BBVA Banco continental'), ('bcp', 'Banco de Crédito del Perú'), ('interbank', 'Interbank')], max_length=32)),
                ('number', models.CharField(max_length=256)),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', related_query_name='bank_account', to='site.SiteSettings')),
            ],
            options={
                'unique_together': {('site_settings', 'number')},
            },
        ),
    ]