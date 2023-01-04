# Generated by Django 4.1.2 on 2023-01-04 13:24

from django.db import migrations, models
import django.db.models.deletion
import products.services


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_rename_path_to_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                upload_to=products.services.upload_media_path,
                verbose_name="image",
            ),
        ),
        migrations.CreateModel(
            name="ProductVideo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "video",
                    models.ImageField(
                        upload_to=products.services.upload_media_path,
                        verbose_name="video",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="videos", to="products.product"
                    ),
                ),
            ],
            options={
                "db_table": "product_videos",
            },
        ),
    ]