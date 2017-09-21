from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    birth_day = models.DateField(verbose_name=u'birthday', null=True, blank=True)
    gend = models.CharField(choices=(('m', 'male'), ('f', 'female')), default='m', max_length=4, verbose_name=u'gender')
    address = models.CharField(max_length=100, null=True, verbose_name=u'address')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', null=True, blank=True)

    class Meta:
        verbose_name = u'User Profile'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
