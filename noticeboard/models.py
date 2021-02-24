from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Notice(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    exp_date = models.DateTimeField('Expiration date')
    body = models.TextField(max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, max_length=1)
    # hidden = models.BooleanField(default=False)
    # attachment = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('noticeboard:single-notice', kwargs={'pk': self.pk})

    def has_expired(self):
        return self.exp_date <= timezone.now()
