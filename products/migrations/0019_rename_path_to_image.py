from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0018_product_change_images_table_name"),
    ]

    operations = [migrations.RenameField("ProductImage", "path", "image")]
