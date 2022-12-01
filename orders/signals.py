from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order
from .tasks import notify


@receiver(post_save, sender=Order)
def order_created(sender, instance, **kwargs):
    notify.delay(instance.id)
