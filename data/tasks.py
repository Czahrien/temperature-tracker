from __future__ import absolute_import, unicode_literals

from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)

@task(name="send_email_task")
def send_email_task(subject, body, from_address, to_addresses):
    send_mail(subject, body, from_address, to_addresses, fail_silently=False)