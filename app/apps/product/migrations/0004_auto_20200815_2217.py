# Generated by Django 3.0.7 on 2020-08-15 22:17

import apps.product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200815_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[apps.product.models.validate_file_extension], verbose_name='Imagen'),
        ),
    ]
