# Generated by Django 4.1.2 on 2022-12-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0014_alter_productsspecifications_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="images",
            options={"ordering": ["position"]},
        ),
        migrations.AddField(
            model_name="images",
            name="position",
            field=models.PositiveIntegerField(default=0, verbose_name="position"),
        ),
    ]
