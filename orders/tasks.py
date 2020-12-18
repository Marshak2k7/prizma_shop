from celery import task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from .models import Order
from online_shop.settings import EMAIL_HOST_USER


logger = get_task_logger(__name__)


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """

    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order. \n' \
              f'The order cost is ${order.get_total_cost()}\n' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          EMAIL_HOST_USER,
                          # 'admin@info.com',
                          [order.email])
    logger.info('Email sent')
    return mail_sent
