from django.contrib import admin
from teacherapp.models import CourseModel,StudentModel,TeacherModel
# Register your models here.
@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','crs_name','crs_fee')

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','course','s_name','s_address','s_gender','s_phone','s_email','joindate')

@admin.register(TeacherModel)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','teacher','course','t_address','t_age','t_gender','t_phone','t_image')