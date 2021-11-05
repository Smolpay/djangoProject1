

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from encrypted_fields.fields import EncryptedCharField




class TableKey(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forWhat = models.CharField(max_length=200, blank=True)
    password = EncryptedCharField(max_length=200, blank=True)
    specification = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.forWhat



