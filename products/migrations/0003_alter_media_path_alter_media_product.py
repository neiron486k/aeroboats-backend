# Generated by Django 4.1 on 2022-08-30 15:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import config.validators


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_options_product_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="path",
            field=models.FileField(
                upload_to="product",
                validators=[
                    django.core.validators.FileExtensionValidator(allowed_extensions=["png", "webp", "mp4", "mpv"]),
                    config.validators.validate_file_size,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="media",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="media",
                to="products.product",
            ),
        ),
    ]
