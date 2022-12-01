from celery import shared_task
from .models import Order
from .services import send_order_to_email


@shared_task()
def notify(order_id: int) -> None:
    order = Order.objects.get(pk=order_id)
    send_order_to_email(order, ['efsneiron@gmail.com'])
