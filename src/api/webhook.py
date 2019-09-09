from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse

from .models import Intent, Utter, Story

import requests


@receiver([post_save, post_delete], sender=Story)
@receiver([post_save, post_delete], sender=Intent)
@receiver([post_save, post_delete], sender=Utter)
def stories_webhook(sender, instance, **kwargs):
    data = webhook_data('stories', reverse('stories-file', kwargs={'project_id': instance.project.id}))
    
    for url in settings.WEBHOOK_URLS:
        try:
            requests.post(url)
        except Exception as e:
            print(f'An error ocurred during webhook communication {e}!')


#@receiver([post_save, post_delete], sender=Intent)
#@receiver([post_save, post_delete], sender=Story)
def actions_webhook(sender, instance, **kwargs):
    data = webhook_data('actions', ACTIONS_URL)
    [requests.post(url, data) for url in settings.WEB_HOOK_URLS] 


def intent_webhook():
    pass


def domain_webhook():
    pass


def webhook_data(content, url):
    return {content: url}
