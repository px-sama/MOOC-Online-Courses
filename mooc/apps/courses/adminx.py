import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = 'Mooc Backend Management System'
    site_footer = 'mooc online'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree_level', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree_level', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree_level', 'learn_time', 'students']
    list_editable = ['degree_level', 'desc']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name ', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'download', 'desc']
    list_filter = ['course', 'desc', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)