from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from storages.backends.gcloud import GoogleCloudStorage
from tinymce import models as tinymce_models

storage = GoogleCloudStorage()

class Post(models.Model):
  title = models.CharField(max_length=100, unique=True)
  body = tinymce_models.HTMLField()
  slug = models.SlugField(unique=True, blank=True)
  date_created = models.DateTimeField()
  date_modified = models.DateTimeField()
  header_img = models.ImageField(upload_to='header_imgs')

  def save(self, *args, **kwargs):
    self.slug=slugify(self.title)
    if self.date_created == None:
      self.date_created = datetime.now()
    self.date_modified = datetime.now()
    super(Post, self).save(*args,**kwargs)

  def __str__(self):
    return self.title


class Page(models.Model):
  title = models.CharField(max_length=12, unique=True)
  body = tinymce_models.HTMLField()
  external_url = models.URLField()


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username
