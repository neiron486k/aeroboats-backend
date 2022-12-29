from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order


def send_order_to_email(order: Order, emails: list[str]) -> None:
    """Send an order to the list of emails with template"""

    body = render_to_string("email/order.html", {"order": order})
    message = EmailMultiAlternatives(
        subject="Новый заказ " + order.product.name,
        to=emails,
    )
    message.attach_alternative(body, "text/html")
    message.send(fail_silently=False)


def order_create(data: dict) -> Order:
    order = Order(**data)
    order.price = order.product.price
    order.save()

    return order
