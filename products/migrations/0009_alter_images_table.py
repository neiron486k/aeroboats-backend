# Generated by Django 4.1.2 on 2022-10-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_images_product_image_delete_media_images_product"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="images",
            table="product_images",
        ),
    ]