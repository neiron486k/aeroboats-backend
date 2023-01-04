from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_alter_product_price"),
    ]

    operations = [
        migrations.RenameModel("Images", "ProductImage"),
    ]
