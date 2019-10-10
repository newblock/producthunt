from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

    title = models.CharField(default='程序类型',max_length=50)
    intro = models.TextField(default='项目介绍')
    icon  = models.ImageField(default='defaultIC.png',upload_to='images/')
    image = models.ImageField(default='defaultIM.png',upload_to='images/')

    votes = models.IntegerField(default='1')
    pub_date = models.DateTimeField()

    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title