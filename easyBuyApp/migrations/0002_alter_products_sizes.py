# Generated by Django 5.1.1 on 2024-09-28 10:53

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyBuyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=50, null=True),
        ),
    ]