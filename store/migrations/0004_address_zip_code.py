# Generated by Django 4.0.4 on 2022-04-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
