from django.db import models

from datetime import datetime

# Create your models here.


class cfinote(models.Model):
    account = models.CharField(max_length=20, primary_key=True, verbose_name='Account')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Time')
    last_modify = models.DateTimeField(verbose_name='Last Modify Time')
    last_access = models.DateTimeField(verbose_name='Last Access Time')
    ExistFlag = models.BooleanField(default=False)
    OrderFlag = models.BooleanField(default=False)
    size = models.BigIntegerField(default=0, verbose_name='Size')

    class Meta:
        verbose_name = 'CFI Account'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.account


class patch(models.Model):
    id = models.CharField(max_length=20, verbose_name='ID')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Time')
    start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
    start_mail = models.CharField(choices=(('y', 'Send'), ('n', 'Not send')), default='n', max_length=2)
    end_time = models.DateTimeField(verbose_name='End Time', null=True, blank=True)
    end_mail = models.CharField(choices=(('y', 'Send'), ('n', 'Not send')), default='n', max_length=2)
    is_active = models.BooleanField(default=False, verbose_name='Active')
    notice = models.CharField(max_length=500, default='', null=True, blank=True, verbose_name='Description')
    size = models.BigIntegerField(default=0, verbose_name='Size')

    class Meta:
        verbose_name = 'Deviation'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.id
