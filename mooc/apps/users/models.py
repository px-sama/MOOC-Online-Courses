from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from datetime import datetime


GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female')
)


class UserProfile(AbstractUser):

    # username = models.CharField(max_length=100, verbose_name='user_name', unique=True)
    # USERNAME_FIELD = 'username'
    # email = models.CharField(max_length=100, verbose_name='email', unique=True)

    nickname = models.CharField(max_length=50, verbose_name='nick_name', default='')
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='gender', choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name='address', default='')
    # unique=True indicates that mobile number is used to identify users
    mobile = models.CharField(max_length=11, verbose_name='mobile number')
    image = models.ImageField(upload_to='head_image/%Y/%m', default='default.jpg')

    # REQUIRED_FIELDS = ['email']

    # objects = UserManager()

    class Meta:
        verbose_name = 'user_info'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username

# Create your models here.


class BaseModel(models.Model):
    # Don't call datetime.now() method inside the class
    # Use datetime.now instead. Otherwise the time will be wrong because it's the time the Course class is instantiated.
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Time ')

    class Meta:
        abstract = True
