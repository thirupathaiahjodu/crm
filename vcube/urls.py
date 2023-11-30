
from django.urls import path
from.import views


urlpatterns=[
    path('',views.homefun,name='homeurl'),
    path('adminp/',views.adminpfun,name='adminpurl'),
    path('courses/',views.coursesfun,name='coursesurl'),
    path('coursedetails/<str:cname>',views.coursedetailsfun,name='coursedetailsurl'),
    path('demos/',views.demosfun,name='demosurl'),
    path('about/',views.aboutfun,name='abouturl'),
    path('contact/',views.contactfun,name='contacturl'),
    path('services/',views.student_inquiry,name='servicesurl'),
    path('enroll/',views.enrollfun,name='enrollurl'),
    path('login/',views.loginfun,name='loginurl'),
    path('logout/',views.logoutfun,name='logouturl'),
   

   
    #Servicess-----------------------
    path('activity/',views.activityfun,name='activityurl'),


    #admin-----
    path('enrollstd/',views.enrollstdfun,name='enrollstdurl'),
    path('add_user/',views.add_user,name='add_user'),
    


    #enroll student----
    path('addstd/',views.addstdfun,name='addstdurl'),
    path('moverecord/<int:s_id>',views.moverecord,name='moverecordurl'),
    path('remove/<int:r_id>',views.removefun,name='removeurl'),
    path('removed/<int:t_id>',views.removedfun,name='removedurl'),
    path('demoaddended/',views.demoattendedfun,name='demoattendedurl'),
    path('delete/',views.deletefun,name='deleteurl'),
    

    #Demos_record-------
    path('demorecord/',views.demorecordfun,name='demorecordurl'),
    path('adddemos/',views.adddemosfun,name='adddemosurl'),
    path('adduser/',views.add_user,name='adduserurl'),


    # student_deatils-------------
    path('upload-interview-data/',views.upload_interview_data,name='upload_interview'),
    path('upload-test-data/',views.upload_test_data, name='upload_test_data'),
    path('upload-attendance-data/',views.upload_attendance_data,name='upload_attendance'),
    path('addstudent/',views.addstudentfun,name='addstudenturl'),
    path('studentdetails/',views.studentdetailsfun,name='studentdetailsurl'),
    path('studentp/<int:student_id>/',views.studentpfun,name='studentpurl'),
    path('test/',views.weekly_test,name='testurl'),
    path('interview/',views.interview,name='interviewurl'),
    path('attadance/',views.attadance,name='attadanceurl'),


    # student Profile page
    path('studentprofile/',views.studentprofile,name='studentprofileurl'),
    


    # reviews---------------
    # path('addreview/',views.addreviewfun,name='addreviewurl'),
    # path('reviews/',views.reviewsfun,name='reviewsurl'),
    path('reviews/', views.show_reviews, name='show_reviews'),
    path('addreview/', views.add_review, name='addreviewurl'),
    path('deletereview/<int:review_id>/',views.delete_review, name='deletereview'),
    path('editreview/<int:review_id>/', views.edit_review, name='editreviewurl'),



    #colabrations--------------------------
    path('addcolabrations/',views.addcolabrationsfun,name='addcolabrationsurl'),
    path('colabrations/',views.colabrationsfun,name='colabrationsurl'),


    #placed students-------------------------
    path('addplacedstd',views.addplacedstdfun,name='addplacedstdurl'),
    path('placedstd/',views.placedstdfun,name='placedstdurl'),


    #ourteam-----------------------------------
    path('addourteam/',views.addourteamfun,name='addourteamurl'),
    path('ourteam/',views.ourteamfun,name='ourteamurl'),


    # Success URL
    path('success/',views.success, name='success_url'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_password/done/', views.password_change_done, name='password_change_done'),

    

    
  
]
