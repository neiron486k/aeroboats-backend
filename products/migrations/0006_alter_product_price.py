# Generated by Django 4.1 on 2022-09-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_media_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name="price"),
        ),
    ]
