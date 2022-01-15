from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher

# Create your models here.

"""
     Design table structure
     1. Define object to object relationships
        1 to 1 or 1 to multiple
        (eg. course -> chapters)
        (chapter -> videos) 
        
        ** Include add_time for each objects
        ** Very usefuly for debugging or log analysis 
        
     2. Objects length  
     3. Onjects type (required or not) 
     
"""


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='teacher')
    name = models.CharField(verbose_name='Course Name', max_length=50)
    desc = models.CharField(verbose_name='Course Description', max_length=300)
    # Store the least unit for times to store in DB
    learn_time = models.IntegerField(default=0, verbose_name='Learn Time')
    degree_level = models.CharField(verbose_name='Difficulty Level', choices=(('beg', 'beginner'),
                                                                             ('intm', 'intermediate'),
                                                                             ('exp', 'expert')), max_length=100)

    students = models.IntegerField(default=0, verbose_name='number of students')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    click_nums = models.IntegerField(default=0, verbose_name='click numbers')
    category = models.CharField(default=u'Backend Dev', max_length=20, verbose_name='course category')
    tag = models.CharField(default='', max_length=10, verbose_name='course tag')
    course_info = models.CharField(default='', max_length=300, verbose_name='course info')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='teach tell')

    detail = models.TextField(verbose_name='Course Detail Information')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='Profile Picture', max_length=100)

    class Meta:
        verbose_name = 'Course Information'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 1 to many, use foreign keys
# on_delete means if the foreignkey  is deleted, what should the current data do?
# if Course is deleted, what should we do with the lessons
# CASCADE will delete any keys cascased eith the foreignkey
# SET_NULL will set keys to Null. (Must be used with null=True, blank=True)


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'chapter name')
    learn_time = models.IntegerField(default=0, verbose_name=u'learning time (mins)')

    class Meta:
        verbose_name = 'Course Chapters'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'video name')
    learn_time = models.IntegerField(default=0, verbose_name=u'learning time (mins)')
    url = models.CharField(max_length=200, verbose_name=u'learning time (mins)')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')
    name = models.CharField(max_length=100, verbose_name=u'name')
    file = models.FileField(upload_to='course/resources/%Y%m', verbose_name='download address', max_length=200)

    class Meta:
        verbose_name = 'Course Resources'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name








