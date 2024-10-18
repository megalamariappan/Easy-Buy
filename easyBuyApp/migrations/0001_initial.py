# Generated by Django 5.1.1 on 2024-09-25 11:19

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('pattern', models.CharField(blank=True, max_length=100, null=True)),
                ('netquantity', models.IntegerField(blank=True, null=True)),
                ('sizes', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'small'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten')], max_length=50, null=True)),
                ('country_origin', models.CharField(max_length=100)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyBuyApp.categories')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyBuyApp.offer')),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyBuyApp.products')),
            ],
        ),
    ]
