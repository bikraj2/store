# Generated by Django 4.0.4 on 2022-04-28 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip_code'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO  store_collection (title)
                VALUES ('collection1')
        """,
        """
        DELETE FROM store_collection 
        where title = 'collection1'
        """)
    ]
