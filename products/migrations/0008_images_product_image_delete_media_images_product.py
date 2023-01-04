# Generated by Django 4.1.2 on 2022-10-29 11:53

import config.validators
from django.db import migrations, models
import django.db.models.deletion
import products.services


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_media_is_cover_alter_media_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "path",
                    models.ImageField(
                        upload_to=products.services.upload_media_path,
                        validators=[config.validators.validate_file_size],
                        verbose_name="path",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default="",
                upload_to=products.services.upload_media_path,
                validators=[config.validators.validate_file_size],
                verbose_name="image",
            ),
        ),
        migrations.DeleteModel(
            name="Media",
        ),
        migrations.AddField(
            model_name="images",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="images", to="products.product"
            ),
        ),
    ]
