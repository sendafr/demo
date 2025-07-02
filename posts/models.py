from django.db import models
from account.models import Account
from giox.models import upload_location
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    liked = models.ManyToManyField(Account, blank=True)
    
    update = models.DateTimeField(auto_now=True, verbose_name="update")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")

    def __str__(self):
        return str(self.title)