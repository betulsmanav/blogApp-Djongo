from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
import uuid

def get_random_code():
    code=str(uuid.uuid4())[:12].replace("-", "")
    return code

@receiver(pre_save, sender=Post)
def slug_create(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug= slugify(instance.title + " " + get_random_code())