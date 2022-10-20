from django.db import models


# Create your models here.
class BookView(models.Model):
    title = models.CharField(verbose_name='书名', max_length=32)
    author = models.CharField(verbose_name='作者', max_length=32)
    pub_date = models.DateField(verbose_name='出版日期')
