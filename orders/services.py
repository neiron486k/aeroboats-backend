from django.core.mail import EmailMessage
from .models import Order


def send_order_to_email(order: Order, emails: list[str]) -> None:
    """Send an order to the list of emails with template"""
    message = EmailMessage(
        "У вас новый заказ", "<strong>test</strong>", "no-replay@aeroglissers.ru", emails
    )
    message.send(fail_silently=False)
