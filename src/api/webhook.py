from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import Intent, Utter, Story

import requests

DOMAIN_URL = ''
ACTIONS_URL = ''

@receiver([post_save, post_delete], sender=Intent)
@receiver([post_save, post_delete], sender=Utter)
def domain_webhook(sender, instance, **kwargs):
    data = webhook_data('domain', DOMAIN_URL)
    [requests.post(url) for url in settings.WEBHOOK_URLS] 


#@receiver([post_save, post_delete], sender=Intent)
#@receiver([post_save, post_delete], sender=Story)
def actions_webhook(sender, instance, **kwargs):
    data = webhook_data('actions', ACTIONS_URL)
    [requests.post(url, data) for url in settings.WEB_HOOK_URLS] 


def intent_webhook():
    pass


def stories_webhook():
    pass


def webhook_data(content, url):
    return {content: url}
