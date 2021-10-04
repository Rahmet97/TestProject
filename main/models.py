from os.path import splitext

from django.contrib.auth.models import User
from transliterate.utils import slugify

from django.db import models


def slugify_upload(instance, filename):
    folder = instance._meta.model.__name__
    name, ext = splitext(filename)
    try:
        name_t = slugify(name)
        if name_t is None:
            name_t = name
        path = folder + "/" + name_t + ext
    except:
        path = folder + "/default" + ext
    return path


class Users(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to=slugify_upload)
    b_date = models.DateField()

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.phone


class New(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to=slugify_upload)
    desc = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
