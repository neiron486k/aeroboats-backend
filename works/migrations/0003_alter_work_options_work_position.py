# Generated by Django 4.1.2 on 2022-12-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("works", "0002_work_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="work",
            options={"ordering": ["position"], "verbose_name": "work", "verbose_name_plural": "works"},
        ),
        migrations.AddField(
            model_name="work",
            name="position",
            field=models.PositiveIntegerField(default=0, verbose_name="position"),
        ),
    ]