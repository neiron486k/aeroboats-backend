# Generated by Django 4.1 on 2022-09-06 15:45

import config.validators
import django.core.validators
from django.db import migrations, models
import products.services


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="media",
            name="is_cover",
            field=models.BooleanField(default=False, verbose_name="cover"),
        ),
        migrations.AlterField(
            model_name="media",
            name="path",
            field=models.FileField(
                upload_to=products.services.upload_image_path,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png", "webp", "jpg", "jpeg", "mp4", "mpv"]
                    ),
                    config.validators.file_size,
                ],
                verbose_name="path",
            ),
        ),
    ]
