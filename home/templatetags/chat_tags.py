from django import template
from ..models import Message

register = template.Library()

@register.simple_tag
def unseen_messages_count(chat, profile):
    return Message.objects.filter(chat=chat, receiver=profile, seen=False).count()
