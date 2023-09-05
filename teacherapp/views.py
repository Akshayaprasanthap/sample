from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')


def admin_home_page(request):
    return render(request,'adminhome.html')   

def admintop(request):
    return render(request,'admintop.html')  

 

def coursepage(request):
    return render(request,'addcourse.html')


def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefee=request.POST['coursefee']
        data = CourseModel(crs_name=coursename,crs_fee=coursefee)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('coursepage')

def login_page(request):
    return render(request,'signin.html')   


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home_page')
            else:
              
                auth.login(request,user)
                return redirect('teacherdetails',user.id)
        else:
            return redirect('login_page')
    return redirect('login_page')






def signup(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context)


def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        address=request.POST['address']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        image=request.FILES.get('file')

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email already exists!!!!')

            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")

                data=User.objects.get(id=user.id)
                teacher_data=TeacherModel(t_address=address,t_age=age,t_gender=gender,t_phone=phone,t_image=image,course=course,teacher=data)
                teacher_data.save()
                # messages.success(request,'welcome....'+data.first_name)
                return redirect('login_page')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login_page')
    else:
        return render(request,'signup.html')



   
def show_teacher(request):
    teacher=TeacherModel.objects.all()
    return render(request,'showteacher.html',{'teacher':teacher})
    


def editpage(request,pk):
    course=CourseModel.objects.all()
    teacher=TeacherModel.objects.get(id=pk) #.....select * from tablename where id = 7;
    return render(request,'editprofile.html',{'teacher':teacher,'course':course})



def edit_teacher_details(request,pk):
    if request.method=='POST':
        teacher = TeacherModel.objects.get(teacher=pk)
        user=User.objects.get(id=pk)
        old=teacher.t_image
        new=request.FILES.get('file')
        if old !=None and new==None:
            teacher.t_image=old
        else:
            teacher.t_image=new
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        # user.username=request.POST.get('Username')
        user.email = request.POST.get('email')
        user.save()
        teacher.t_address = request.POST.get('address')
        teacher.t_age = request.POST.get('age')
        teacher.t_gender = request.POST.get('gender')
        teacher.t_phone = request.POST.get('phone')
        
        crsSelect=request.POST["course"] 
        course=CourseModel.objects.get(id=crsSelect)
        teacher.course=course
        # teacher.course = CourseModel.objects.get(id= request.POST.get('course'))
        teacher.save()
        
        return redirect('teacherdetails',request.user.id)
    return render(request,'editprofile.html',)


def teacherdetails(request,pk):
    teacher=TeacherModel.objects.get(teacher=pk) #.....select * from tablename where id = 7;
    return render(request,'teacherprofile.html',{'teacher':teacher})

def s_details(request,pk):
    if request.method=='POST':
        teacher = TeacherModel.objects.get(id=pk)
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.user_name=request.POST.get('user_name')
        teacher.address = request.POST.get('address')
        teacher.age = request.POST.get('age')
        teacher.gender = request.POST.get('gender')
        teacher.phone = request.POST.get('phone')
        teacher.email = request.POST.get('email')
        teacher.course = request.POST.get('course')
        teacher.image=request.FILES.get('file')
        teacher.save()
        return redirect('teacherdetails')
    return render(request,'teacherprofile.html')


    
def teacher_home_page(request):
    return render(request,'teacherhome.html')   
                    
def teacher(request):
    return render(request,'teacher.html')  


def deletepage_t(request,pk):
    teacher=TeacherModel.objects.get(id=pk)
    return render(request,'delete.html',{'teacher':teacher})

def delete_t(request,pk):
    teacher=TeacherModel.objects.get(id=pk)
    teacher.delete()
    return redirect('show_teacher')





#####################  STUDENT  ################################



def StudentPage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'addstudent.html',context)


def AddStudent(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        stdgender=request.POST['stdgender']
        stdphone=request.POST['stdphone']
        stdemail=request.POST['stdemail']
        joindate=request.POST['joindate']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(s_name=stdname,s_address=stdaddress,s_gender=stdgender,s_email=stdemail,s_phone=stdphone,joindate=joindate,course=course)
        data.save()
        return redirect('admin_home_page')
    
def show_student(request):
    student=StudentModel.objects.all()
    return render(request,'showstudent.html',{'student':student})


# def stud(request,pk):
#     student=StudentModel.objects.get(id=pk) #.....select * from tablename where id = 7;
#     return render(request,'showstudent.html',{'student':student})

# def stud_details(request,pk):
#     if request.method=='POST':
#         student = StudentModel.objects.get(id=pk)
#         student.stdname = request.POST.get('stdname')
#         student.stdaddress = request.POST.get('stdaddress')
#         student.stdgender = request.POST.get('stdgender')
#         student.stdphone = request.POST.get('stdphone')
#         student.stdemail = request.POST.get('stdemail')
#         student.course = request.POST.get('course')
#         student.save()
#         return redirect('show_student')
#     return render(request,'showstudent.html',)
    





def deletepage(request,pk):
    student=StudentModel.objects.get(id=pk)
    return render(request,'delete.html',{'student':student})

def delete_std(request,pk):
    student=StudentModel.objects.get(id=pk)
    student.delete()
    return redirect('show_student')






def logout(request):
	auth.logout(request)
	return redirect('index')