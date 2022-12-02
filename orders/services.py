from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Order


def send_order_to_email(order: Order, emails: list[str]) -> None:
    """Send an order to the list of emails with template"""

    body = render_to_string("orders/email/order.html", )
    message = EmailMultiAlternatives(
        subject="Новый заказ на " + order.product.name,
        to=emails
    )
    message.attach_alternative(body, "text/html")
    message.send(fail_silently=False)
