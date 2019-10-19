# Generated by Django 2.2 on 2019-04-17 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0022_auto_20190413_2016'),
        ('page', '0007_auto_20190225_0252'),
        ('store', '0002_socialnetwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('about', 'About'), ('faq', 'FAQ'), ('legal', 'Terms and Conditions'), ('privacy', 'Privacy and Cookies'), ('accessibility', 'Accessibility')], max_length=32)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_settings', related_query_name='site_setting', to='page.Page')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_pages', related_query_name='special_page', to='site.SiteSettings')),
            ],
            options={
                'unique_together': {('site_settings', 'type')},
            },
        ),
    ]