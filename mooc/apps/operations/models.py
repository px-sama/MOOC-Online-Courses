from django.db import models

from django.contrib.auth import get_user_model
from apps.users.models import BaseModel
from apps.courses.models import Course
# Create your models here.

UserProfile = get_user_model()


class UserInquiry(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'name')
    mobile = models.CharField(max_length=11, verbose_name=u'phone number')
    course_name = models.CharField(max_length=50, verbose_name=u'course name')

    class Meta:
        verbose_name = 'User Inquiry'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{name}_{course}({mobile})'.format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE )
    comments = models.CharField(max_length=200, verbose_name='comments')

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    # This is not a good way to maintain database
    # Laster if we need to scale the projects to include more fields, we need to change the table
    # course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Course, verbose_name='teacher ', on_delete=models.CASCADE)

    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name='favorite id')
    fav_type = models.IntegerField(choices=((1, 'lessons'), (2, 'organization'), (3, 'Teachers')), default=1,
                                   verbose_name='fav type')

    class Meta:
        verbose_name = 'User Favorite'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}_{id}'.format(user=self.user, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    message = models.CharField(max_length=200, verbose_name='message')
    has_read = models.BooleanField(default=False, verbose_name=u'has read')

    class Meta:
        verbose_name = 'User Message'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Course   '
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name




