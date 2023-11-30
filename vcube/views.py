from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from django.contrib import messages
from . forms import *
from django.contrib.auth import authenticate,login,logout
from . models import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import pandas as pd
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review, Colabrations, Ourteam, Recent_Placed
from .forms import NewStudentForm

def homefun(request):
    review = Review.objects.all().order_by('-pk')[:5]  # Fetch the latest 5 records
    company = Colabrations.objects.all().order_by('-pk')[:10]
    placed = Recent_Placed.objects.all().order_by('-pk')[:5]

    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Check if there are more than 5 records and delete the oldest one if necessary
            if review.count() > 5:
                oldest_review = review.last()
                oldest_review.delete()

            if company.count() > 10:
                oldest_company=company.last()
                oldest_company.delete()

            if placed.count() > 5:
                oldest_placed = placed.last()
                oldest_placed.delete()

            


            messages.success(request, 'Data saved successfully.')
            return redirect('homeurl')
        else:
            messages.error(request, 'Failed to create student. Please check the form data.')
    else:
        form = NewStudentForm()

    return render(request, 'vcube/home.html', {'form': form,  'company': company, 'placed': placed, 'review': review})

def adminpfun(request):
    obj=newstudent.objects.all()
    return render(request,'vcube/admin.html',{'data':obj})

def coursesfun(request):
    data=Courses.objects.all()
    return render(request,'vcube/courses.html',{'data':data})

def coursedetailsfun(request,cname):
    data=Courses.objects.filter(cname=cname)
    if request.method=='POST':
        form=NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'data saved succesfully.')
            return redirect('coursedetailsurl')
        else:
            messages.error(request, 'Failed to create student. Please check the form data.') 
    else:
        form=NewStudentForm()
    return render(request,'vcube/coursedetails.html',{'data':data,'form':form})


def demosfun(request):
    obj = Demos.objects.all().order_by('-pk')  # Ordering by the primary key in reverse order
    if request.method == 'POST':
        form = DemosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminurl')
    else:
        form = DemosForm()
    return render(request, 'vcube/demo.html', {'data': obj, 'form': form})

def aboutfun(request):
    team=Ourteam.objects.all()
    return render(request,'vcube/about.html',{'team':team})


def contactfun(request):
    if request.method=='POST':
        form=NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeurl')
    else:
        form=NewStudentForm()
    return render(request,'vcube/contact.html',{'form':form})

def student_inquiry(request):
    
    if request.method == 'POST':
        data = StudentInquiryForm(request.POST)
        if data.is_valid():
           data.save()
           return HttpResponse('data saved successfully')  # Redirect to a success page
        else:
            return HttpResponse('error')
    else:
        data = StudentInquiryForm()

    return render(request, 'vcube/services.html', {'form': data})
   

def enrollfun(request):
    if request.method=='POST':
        form=NewStudentForm(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request,'data saved successfully.')
            return redirect('enrollurl')
        else:
             messages.error(request, 'Failed to create student. Please check the form data.')
    else:
        form=NewStudentForm()

    return render(request,'vcube/enroll.html',{'form':form})



# def loginfun(request):
#     try:
#         if request.method == 'POST':
#             uname = request.POST['uname']
#             pwd = request.POST['password']
#             valid_user = authenticate(username=uname,password=pwd)

#             if valid_user is not None:
#                 login(request, valid_user)

#                 if valid_user.is_superuser:
#                     return redirect('adminurl')

#                 elif valid_user.is_staff:
#                     return redirect('adminurl')

#                 elif valid_user.is_active:
#                     return redirect('studentpurl')

#                 else:
#                     return HttpResponse('User not defined')

#             else:
#                 error_message = 'Wrong password 🙄 Please check the password and try again..!!!!'
#                 login_url = reverse('loginurl')
#                 return render(request, 'main/login.html',
#                               {'error_message': error_message, 'loginurl': login_url})

#         return render(request, 'main/login.html', {'loginurl': reverse('loginurl')})
#     except Exception as e:
#         return HttpResponse("Error: " + str(e))




def loginfun(request):

    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['password']
        valid_user=authenticate(request,username=uname,password=pwd)

        if valid_user != None:
            login(request,valid_user)

            if valid_user.is_superuser: 
                # Super user login
                return redirect('adminpurl')
            elif valid_user.is_staff:   
                # staff user login
                return redirect('adminpurl')
            elif valid_user.is_active:
                return redirect('studentprofileurl')

            else:                       
                # Student login
                return redirect('user not defined')
        
        else:
            error_message = 'Wrong password Please check the password and try again..'
            login_url = reverse('loginurl')
            return render(request, 'vcube/login.html', {'error_message': error_message, 'loginurl': login_url})
        
    return render(request, 'vcube/login.html', {'loginurl': reverse('loginurl')})

def logoutfun(request):
    try:
        logout(request)
        return redirect('loginurl')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def reviewfun(request):
    return render(request,'vcube/review.html')

#Servicess--------------------------------------
def activityfun(request):
    return render (request,'Services/ouractivity.html')   
    

#admin-----
def enrollstdfun(request):
    obj=newstudent.objects.all()
    return render(request,'admin/enroll_student/enrollstd.html',{'data':obj})


#enroll student------
def addstdfun(request):
    if request.method=='POST':
        form=NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form=NewStudentForm()
    return render(request,'admin/enroll_student/addstd.html',{'form':form})

# MOVING RECORD FROM ENROLL TABLE TO DEMO TABLE ------
def moverecord(request,s_id):
    specific_record=newstudent.objects.get(id=s_id)
    destination_record=demoattended.objects.create(
        Name=specific_record.Name,
        Email=specific_record.Email,
        Mobile_Number=specific_record.Mobile_Number,
        Courses=specific_record.Courses,
        Training=specific_record.Training)
    specific_record.delete()
    return redirect('enrollstdurl')

# DELETING  RECORD FROM ENROLL TABLE TO DELETED TABLE -----------

def removefun(request,r_id):
    obj=newstudent.objects.get(id=r_id)
    remove_record=deleted.objects.create(
        Name=obj.Name,
        Email=obj.Email,
        Mobile_Number=obj.Mobile_Number,
        Courses=obj.Courses,
        Training=obj.Training)
    obj.delete()
    return redirect('enrollstdurl')


# Moving record from  demo table to confirm table------------------
def removedfun(request,t_id):
    obj=demoattended.objects.get(id=t_id)
    remove_record=deleted.objects.create(Name=obj.Name,
        Email=obj.Email,
        Mobile_Number=obj.Mobile_Number,
        Courses=obj.Courses,
        Training=obj.Training)
    obj.delete()
    return redirect('enrollstdurl')
    
#  enroll student demo attendend--------------------
def demoattendedfun(request):
    obj=demoattended.objects.all()
    return render(request,'admin/enroll_student/demoattend.html',{'data':obj})




# enroll student deleted--------------- 
def deletefun(request):
    obj=deleted.objects.all()
    return render(request,'admin/enroll_student/delete.html',{'data':obj})
  


#demo record-------
def demorecordfun(request):
    obj=Demos.objects.all()
    return render(request,'admin/demos_records/demorecords.html',{'data':obj})

def adddemosfun(request):
    if request.method=='POST':
        form=DemosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demorecordurl')
    else:
        form=DemosForm()
    return render(request,'admin/demos_records/adddemos.html',{'form':form})


#student details----------------------------------------------------------------------------------------------------------
def upload_test_data(request):
    try:
        if request.method == 'POST':
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                test_date = row['test_date']
                marks = row['marks']
                student = Student.objects.get(admission_number=admission_number)
                test = Test(student=student, test_date=test_date, marks=marks)
                test.save()

            return HttpResponse('data saved successfully')

        return render(request, 'admin/student_details/upload_test.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))
    

def upload_attendance_data(request):
    try:
        if request.method == 'POST':
            attendance_file = request.FILES['attendance_file']
            df = pd.read_excel(attendance_file)

            attendance_list = []

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                date = row['date']
                present_value = row['present']

                if present_value == 'Yes':
                    present = True
                elif present_value == 'No':
                    present = False
                else:
                    continue

                try:
                    student = Student.objects.get(admission_number=admission_number)
                except Student.DoesNotExist:
                    continue

                attendance = Attendance(student=student, date=date, present=present)
                attendance_list.append(attendance)

            Attendance.objects.bulk_create(attendance_list)

            return HttpResponse('data saved successfully')

        return render(request, 'admin/student_details/upload_attendence.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))
    

def upload_interview_data(request):
    try:
        if request.method == 'POST':
            interview_file = request.FILES['interview_file']
            df = pd.read_excel(interview_file)

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                interview_date = row['interview_date']
                performance = row['performance']
                present_value = row['present']

                if present_value == 'Yes':
                    present = True
                elif present_value == 'No':
                    present = False
                else:
                    continue

                try:
                    student = Student.objects.get(admission_number=admission_number)
                except Student.DoesNotExist:
                    continue

                interview = Interview(student=student, interview_date=interview_date, performance=performance, present=present)
                interview.save()

            return render(request, 'admin_upload/test_success.html')

        return render(request, 'admin/student_details/upload_mockinterviews.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))
    

def weekly_test(request):
    try:
        student = request.user.student
        tests = Test.objects.filter(student=student)

        return render(request, 'admin/student_details/test.html', {'tests': tests, 'student': student})
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def interview(request):
    try:
        student = request.user.student
        interview = Interview.objects.filter(student=student)
        return render(request, 'admin/student_details/mockinterviews.html', {'student': student, 'interview': interview})
    except Exception as e:
        return HttpResponse("Error: " + str(e))
    
def attadance(request):
    try:
        student = request.user.student
        attadance = Attendance.objects.filter(student=student)
        return render(request, 'admin/student_details/attendence.html', {'student': student, 'attadance': attadance})
    except Exception as e:
        return HttpResponse("Error: " + str(e))






def addstudentfun(request):
    try:
        std_info = StudentForm
        course = Courses.objects.all()
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('studentdetailsurl')
            else:
                print(form.errors)

        return render(request,'admin/student_details/addstudent.html', {'form': std_info, 'course': course})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def studentdetailsfun(request) :
    students = Student.objects.all()
    return render(request,'admin/student_details/student.html',{'students': students})

def studentpfun(request,student_id):
    students = get_object_or_404(Student, id=student_id)
    
    return render(request,'admin/student_details/studentp.html',{'students': students})


  

def studentprofile(request):
    student = request.user.student    
    return render(request, 'student_profile/studentprofile.html', {
        'student': student,
        
    })




#reviews----------------------------------------------------------------------------------------------------------------------
# def reviewsfun(request):
#     reviews = Review.objects.all().order_by('-pk')  # Ordering by the primary key in reverse order
#     return render(request, 'admin/reviews/reviews.html', {'review': reviews})

# def addreviewfun(request):
#     obj = ReviewForm()
#     if request.method=='POST':
#         form=ReviewForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('reviewsurl')
#     else:
#         form=ReviewForm()
#         print(form.errors)
#     return render(request,'admin/reviews/addreview.html',{'obj':obj})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'admin/reviews/show_reviews.html', {'reviews': reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_reviews')  # Redirect to the review records page after successful submission
    else:
        form = ReviewForm()
    return render(request, 'admin/reviews/add_review.html', {'form': form})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('show_reviews')  # Redirect to the review records page after successful deletion
    return render(request, 'admin/reviews/delete_review.html', {'review': review})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('show_reviews')  # Redirect to the review records page after successful update
    else:
        form = ReviewForm(instance=review)
    return render(request, 'admin/reviews/edit_review.html', {'form': form, 'review': review})



#colabrations----------------------------------------------------------------------------------------------------------------

def colabrationsfun(request):
    company=Colabrations.objects.all().order_by('-pk')
    return render(request,'admin/colabrations/colabrations.html',{'company':company})

# def addcolabrationsfun(request):
#     if request.method=='POST':
#         form=ColabrationsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect()
#     else:
#         form=ColabrationsForm()
#     return render(request,'admin/colabrations/addcolabrations.html',{'form':form})

def addcolabrationsfun(request):
    if request.method == 'POST':
        form = ColabrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colabrationsurl')  # Redirect to the page displaying the list of collaborations after successful submission
    else:
        form = ColabrationsForm()
    return render(request, 'admin/colabrations/addcolabrations.html', {'form': form})



#placed students------------------------------------------------------------------------------------------------------

def addplacedstdfun(request):
    obj = Recent_PlacedForm()
    if request.method=='POST':
        form=Recent_PlacedForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('placedstdurl')
    else:
        form=Recent_PlacedForm()
        print(form.errors)

    return render(request,'admin/placed_student/addplacedstd.html',{'obj':obj})

def placedstdfun(request):
    placed=Recent_Placed.objects.all().order_by('-pk')
    return render(request,'admin/placed_student/placedstd.html',{'placed':placed})

#Ourteam------------------------------------------------------------------------------------------------------------
def addourteamfun(request):
    return render(request,'admin/ourteam/addourteam.html')
def ourteamfun(request):
    team=Ourteam.objects.all()
    return render(request,'admin/ourteam/ourteam.html',{'team':team})




from django.shortcuts import get_object_or_404
# sending user name and password to user by clicking join button

from django.core.mail import send_mail
from django.contrib.auth.models import User

def add_user(request):
    if request.method == 'POST':
        res_id = request.POST.get('res_id')
        demo = get_object_or_404(demoattended, id=res_id)
        #demo = demoattended.objects.get(id=res_id)
        username = demo.Name.lower().replace(" ", "")
        password = User.objects.make_random_password()
        # Send the username, password, and message to the user via email
        
        message = f'Thank you for Registering into VCube Software Solutions Pvt.Ltd.\n\n'
        message += f'Username: {username}\nPassword: {password}\n\n'
        message += f'Please keep your Credentials Confidential and change your password for security purposes.'
        try:
            send_mail(
                'Your Account Details',
                message,
                'thirupathaiahjodu.gmail.com',
                [demo.Email],
                fail_silently=False,
            )
            demo.status = 'Yes'  # Update the status to 'Yes' if email sent successfully
        except Exception as e:
            demo.status = 'No'  # Update the status to 'No' if there was an error sending the email
                # Handle the exception or display an error message
                

        user = get_user_model().objects.create(
            username=username,
            password=make_password(password),
            email=demo.Email
        )
            
        demo.user = user
        demo.save()

        return HttpResponse('data save sucsess')
        
    return HttpResponseNotAllowed(['POST'])

def success(request):
    return render(request, 'vcube/success.html')




def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('password_change_done')
        
        else:
             messages.error(request, 'Failed to change password. Please check the form data.')

            
    else:
        form = PasswordChangeForm(request.user)
        print(form.errors)

    return render(request, 'admin/student_details/changepassword.html',{'form':form})




# when password is changed successfully                                                                                                            

def password_change_done(request):
    #return redirect('loginurl')
    return render(request, 'admin/student_details//passworddone.html')



