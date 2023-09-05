from django.urls import path
from teacherapp import views
from django.contrib import admin


urlpatterns = [
    path("",views.index,name="index"),
    path("login_page",views.login_page,name="login_page"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("usercreate",views.usercreate,name="usercreate"),
    path("coursepage",views.coursepage,name="coursepage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("StudentPage",views.StudentPage,name="StudentPage"),
    path("AddStudent",views.AddStudent,name="AddStudent"),
    path("show_teacher",views.show_teacher,name="show_teacher"),
    path("editpage/<int:pk>",views.editpage,name="editpage"),
    path("edit_teacher_details/<int:pk>",views.edit_teacher_details,name="edit_teacher_details"),
    path("teacher_home_page",views.teacher_home_page,name="teacher_home_page"),
    path("admin_home_page",views.admin_home_page,name="admin_home_page"),
    path("show_student",views.show_student,name="show_student"),
    path("admintop",views.admintop,name="admintop"),
    path("teacherdetails/<int:pk>",views.teacherdetails,name="teacherdetails"),
    path("s_details/<int:pk>",views.s_details,name="s_details"),
    path("teacher",views.teacher,name="teacher"),
    path('deletepage/<int:pk>',views.delete_std,name='delete_std'),
    path('deletepage_t/<int:pk>',views.delete_t,name='delete_t'),
    path('logout/',views.logout,name="logout")
]