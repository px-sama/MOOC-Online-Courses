from django.db import models
from apps.users.models import BaseModel

# Create your models here.


class City(BaseModel):
    name = models.CharField(max_length=50, verbose_name=u'city name')
    desc = models.TextField(max_length=200, verbose_name=u'description')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name='organization name')
    desc = models.TextField(verbose_name='description')
    tag = models.CharField(default='world famous', max_length=10, verbose_name='organization tag')
    category = models.CharField(default=u'organization', max_length=20, verbose_name='org category',
                                choices=(('third party org', 'third party'), ('individual', 'individual'),
                                         ('college', 'college')))
    click_nums = models.IntegerField(default=0, verbose_name='click num')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite num')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='logo', max_length=100)
    address = models.CharField(max_length=100, verbose_name='address', default='')
    students = models.IntegerField(default=0, verbose_name='student nums')
    course_nums = models.IntegerField(default=0, verbose_name='course nums')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='cities')
    # Organization cities
    # Notice that cities is better defined as a separate class since there might be too many locations around the world

    class Meta:
        verbose_name = 'Course Organization'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='organization')
    name = models.CharField(max_length=50, verbose_name='teacher name')
    work_years = models.IntegerField(default=0, verbose_name='work years')
    work_company = models.CharField(max_length=50, verbose_name='work company')
    work_position = models.CharField(max_length=50, verbose_name='work position')
    style = models.CharField(max_length=50, verbose_name='teaching style')
    click_nums = models.IntegerField(default=0, verbose_name='click num')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite num')
    age = models.IntegerField(default=18, verbose_name='age')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='profile picture', max_length=100)


    class Meta:
        verbose_name = 'Teacher Profile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
