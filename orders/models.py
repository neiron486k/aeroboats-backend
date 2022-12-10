from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from config.validators import full_name
from products.models import Product


class Order(models.Model):
    """Orders of products"""

    full_name = models.CharField(_("full_name"), max_length=255, validators=[full_name])
    phone = PhoneNumberField(_("phone"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        db_table = "order"
        verbose_name = _("order")
        verbose_name_plural = _("orders")
