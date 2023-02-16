from django.db import models

# Create your models here.

class Url(models.Model):
    url=models.CharField(max_length= 500)
    class Meta:
        verbose_name='url'
        verbose_name_plural='urls'
    def __str__(self) -> str:
        return self.url + ' ' + str(self.id)