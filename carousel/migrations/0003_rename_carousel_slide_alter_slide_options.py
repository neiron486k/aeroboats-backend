# Generated by Django 4.1 on 2022-08-22 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carousel", "0002_remove_carousel_image_carousel_thumbnail"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Carousel",
            new_name="Slide",
        ),
        migrations.AlterModelOptions(
            name="slide",
            options={"ordering": ["-id"]},
        ),
    ]
