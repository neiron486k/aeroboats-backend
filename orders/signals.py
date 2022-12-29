from django.dispatch import Signal
from django.dispatch import receiver

from .models import Order
from .tasks import notify

order_created_signal = Signal()


@receiver(order_created_signal)
def order_created(order: Order, **kwargs):
    notify.delay(order.id)
