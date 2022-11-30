from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from products.models import Product
from config.validators import full_name


class Order(models.Model):
    """Orders of products"""

    full_name = models.CharField(_("full_name"), max_length=255, validators=[full_name])
    phone = PhoneNumberField(_("phone"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "order"
        verbose_name = _("order")
        verbose_name_plural = _("orders")
