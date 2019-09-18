from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse

from .models import Intent, Utter, Story

import requests
import json


@receiver([post_save], sender=Story)
@receiver([post_save], sender=Intent)
@receiver([post_save], sender=Utter)
def stories_webhook(sender, instance, **kwargs):
    data = webhook_data('stories', reverse('stories-file', kwargs={'project_id': instance.project.id})) 
    hook(data, 'STORIES')    


@receiver([post_save], sender=Intent)
def intents_webhook(sender, instance, **kwargs):
    data = webhook_data('intents', reverse('intents-file', kwargs={'project_id': instance.project.id}))
    hook(data, 'INTENTS')    


def stories_delete_hook(project_pk):
    data = webhook_data('stories', reverse('stories-file', kwargs={'project_id': project_pk}))
    hook(data, 'STORIES')    


def intents_delete_hook(project_pk):
    data = webhook_data('intents', reverse('intents-file', kwargs={'project_id': project_pk}))
    hook(data, 'INTENTS')    


def domain_delete_hook(project_pk): 
    data = webhook_data('domain', reverse('domain-file'), kwargs={'project_id': project_pk})
    hook(data, 'DOMAIN')


@receiver([post_save], sender=Story)
@receiver([post_save], sender=Intent)
@receiver([post_save], sender=Utter)
def domain_webhook(sender, instance, **kwargs):
    data = webhook_data('domain', reverse('domain-file', kwargs={'project_id': instance.project.id}))
    hook(data, 'DOMAIN')


def hook(data, error):
    for url in settings.WEBHOOK_URLS:
        try:
            requests.post(url, json=data)

        except Exception as e:
            print(f'An error occurred during "{error}" webhook communication {e}!')


def webhook_data(content, url):
    return json.dumps({content: url})
