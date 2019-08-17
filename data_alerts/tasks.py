from __future__ import absolute_import, unicode_literals
from settings import DEFAULT_FROM_EMAIL
from celery.task.schedules import crontab
from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from data.models import Device, TemperatureDataPoint
from data.tasks import send_email_task
from .models import AlertFamily, AlertThreshold

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute="*/1")),
    name="check_alerts_task",
    ignore_result=True)
def check_alerts_task():
    for a in AlertFamily.objects.all():
        next_dp = a.device.datapoints.last().temperaturedatapoint
        next_value = next_dp.temperaturedatapoint.temperature
        for t in a.thresholds.all():
            dp = t.current_datapoint
            if dp.date != next_dp.date:
                current_value = dp.temperaturedatapoint.temperature
                change = True
                if t.threshold_value < current_value and t.threshold_value > next_value:
                    logger.info("falling transition")
                    send_email_task.delay(
                        '"%s" Falling Transition' % (t.name),
                        '%s measured value below threshold %d (Value: %d)' % (
                            t.description, t.threshold_value, next_value),
                        DEFAULT_FROM_EMAIL,
                        [email for m in a.mailing_lists.all() for email in m.get_emails()])
                    change = True
                elif t.threshold_value > current_value and t.threshold_value < next_value:
                    logger.info("rising transition")
                    send_email_task.delay(
                        '"%s" Rising Transition' % (t.name),
                        '%s measured value above threshold %d (Value: %d)' % (
                            t.description, t.threshold_value, next_value),
                        DEFAULT_FROM_EMAIL,
                        [email for m in a.mailing_lists.all() for email in m.get_emails()])
                else:
                    change = False

                t.current_datapoint = next_dp
                t.save()
