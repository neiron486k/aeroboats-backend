from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order


@receiver(post_save, sender=Order)
def create_order_handler(sender, instance, created, **kwargs):
    if created:
        ...
