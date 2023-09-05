from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class CourseModel(models.Model):
    crs_name=models.CharField(max_length=100)
    crs_fee=models.IntegerField()

class StudentModel(models.Model):
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    s_name=models.CharField(max_length=100)
    s_address=models.CharField(max_length=255)
    s_gender=models.CharField(max_length=100)
    s_phone=models.CharField(max_length=255)
    s_email=models.CharField(max_length=255)
    joindate=models.DateField(auto_now_add=True)

class TeacherModel(models.Model):
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    t_address=models.CharField(max_length=100)
    t_age=models.IntegerField()
    t_gender=models.CharField(max_length=100)
    t_phone=models.CharField(max_length=100)
    t_image=models.ImageField(upload_to="image/",null=True)
