from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

def upload_image_event(instance, filename):
    return f"{instance.title}-{str(uuid.uuid4())}-{filename}"


class Event(models.Model):

    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    private = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_image_event, blank=False, null=False)
    date = models.DateField(blank=False ,null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

