from celery import shared_task
from .models import Order
from .services import send_order_to_email
from django.conf import settings


@shared_task()
def notify(order_id: int) -> None:
    order = Order.objects.get(pk=order_id)
    send_order_to_email(order, [settings.DEFAULT_TO_EMAIL])
