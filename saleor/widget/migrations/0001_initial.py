# Generated by Django 2.2 on 2019-04-14 15:24

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0091_auto_20190402_0853'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('homepage', 'Home page'), ('collection', 'Collections'), ('category', 'Categories'), ('brand', 'Brands')], default='homepage', max_length=20)),
                ('name', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=False)),
                ('active_on', models.DateField(blank=True, null=True)),
                ('active_until', models.DateField(blank=True, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('brands', models.ManyToManyField(blank=True, related_name='sliders', related_query_name='slider', to='brand.Brand')),
                ('categories', models.ManyToManyField(blank=True, related_name='sliders', related_query_name='slider', to='product.Category')),
                ('collections', models.ManyToManyField(blank=True, related_name='sliders', related_query_name='slider', to='product.Collection')),
            ],
            options={
                'ordering': ('name',),
                'permissions': (('manage_sliders', 'Manage sliders.'),),
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='slides')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('alt', models.CharField(blank=True, max_length=128)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', related_query_name='slide', to='widget.Slider')),
            ],
            options={
                'ordering': ('sort_order',),
            },
        ),
    ]
