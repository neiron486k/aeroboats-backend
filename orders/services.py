from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order


class OrderService:
    def create(self, data: dict) -> Order:
        order = Order(**data)
        order.price = order.product.price
        order.save()

        from .signals import order_created_signal

        order_created_signal.send(sender=self.__class__, order=order)

        return order


def send_email(order: Order) -> None:
    """Send an email of a created order to the owner"""

    from django.conf import settings

    body = render_to_string("email/order.html", {"order": order})
    message = EmailMultiAlternatives(
        subject="Новый заказ: " + order.product.name,
        to=[settings.DEFAULT_TO_EMAIL],
    )
    message.attach_alternative(body, "text/html")
    message.send(fail_silently=False)
