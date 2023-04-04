from datetime import datetime

from Board.celery import app
from questionnaire.models import Service


@app.task
def check_subscription_date():
    """Check all services on subscription expire"""
    services = Service.objects.all()
    for service in services:
        if datetime.utcnow() > service.subscription_expire:
            service.subscription_active = False
            service.save(update_fields=["subscription_active"])


@app.task
def subscription_inactive(pk):
    """Disable subscription for service with current pk"""
    service = Service.objects.get(pk=pk)
    service.subscription_active = False
    service.save(update_fields=["subscription_active"])
