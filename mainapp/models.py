from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify

# Create your models here.
class UserProfile(models.Model):
    userr = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(default='-', max_length=150)
    email = models.EmailField(default='-', max_length=256, blank=False)
    name = models.CharField(default='-', max_length=150)
    
    def __str__(self):
        return self.username
    

class InFlowAIProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(default='-', max_length=200)
    assistant_prompt = models.TextField(default='-')
    created_at = models.DateTimeField(auto_now_add=True)
    project_link = AutoSlugField(populate_from='project_name', unique=True, slugify=slugify)

    def __str__(self):
        return self.project_name