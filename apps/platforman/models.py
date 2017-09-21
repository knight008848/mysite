from django.db import models

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=45, unique=True, verbose_name='name')
    model = models.CharField(max_length=20, verbose_name='SysID')
    lob = models.CharField(max_length=20, verbose_name='LOB')
    type = models.CharField(max_length=20, verbose_name='Type')
    pebit = models.CharField(max_length=2, default='64', choices=(('64', '64'), ('32', '32')), verbose_name='PE')
    product = models.CharField(max_length=100, null=True, blank=True, verbose_name='Model Name')
    phnum = models.CharField(max_length=20, null=True, blank=True, verbose_name='PH#')

    class Meta:
        verbose_name = 'Platform'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
