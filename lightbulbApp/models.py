from django.db import models
# inbuilt user model pre made by django
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # cascade deletes post if user is removed or deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # sets default title, sets default ordering 

    def __str_(self):
        return self.title

    class Meta:
        ordering = ['created']