# Generated by Django 4.1.2 on 2022-12-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_alter_images_options_images_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(default="", max_length=100, verbose_name="name"),
        ),
    ]
