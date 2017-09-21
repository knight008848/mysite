from django.db import models

from datetime import datetime

# Create your models here.


class gcfnote(models.Model):
    number = models.CharField(max_length=45, unique=True, verbose_name='PO')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Time')
    model = models.CharField(max_length=45, verbose_name='Model')
    family = models.CharField(max_length=45, verbose_name='Platform')
    level = models.CharField(max_length=45, verbose_name='Level')
    region = models.CharField(max_length=45, verbose_name='Region')
    ctomod = models.CharField(max_length=45, verbose_name='Channel')
    dest = models.CharField(max_length=45, verbose_name='Destination')
    OSP = models.CharField(max_length=45)
    OSD = models.CharField(max_length=45)
    OSV = models.CharField(max_length=45)
    muiflag = models.BooleanField(default=False)
    cfiflag = models.BooleanField(default=False)
    siaccount = models.CharField(max_length=45, null=True, blank=True, verbose_name='CFI Account')
    mod = models.TextField(verbose_name='MOD Content')
    sdr = models.TextField(verbose_name='SDR Content')
    filepath = models.CharField(max_length=100, verbose_name='File Path')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Quantity')

    class Meta:
        verbose_name = 'GCF Record'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.number
