from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Courses_Name(models.Model):
    crsid=models.IntegerField(primary_key=True)
    crsname=models.CharField(max_length=20,null=True)
    def __str__(self) -> str:
        return self.crsname
    

class Training(models.Model):
    Name=models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.Name



class newstudent(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile_Number=models.CharField(max_length=12)
    Graduation=models.CharField(max_length=50,null=True)
    Courses=models.ForeignKey(Courses_Name,on_delete=models.CASCADE)
    Training=models.ForeignKey(Training,on_delete=models.CASCADE,null=True)

    
    def __str__(self) :
        return self.Name
    

class Courses(models.Model):
    cname=models.CharField(max_length=25)
    image=models.ImageField(upload_to='images/')
    desrciption=models.TextField(null=True)
    photo=models.ImageField(upload_to='images/',null=True)
    highlights=models.TextField(null=True)
    KeyFutures=models.TextField(null=True)

    def __str__(self):
        return self.cname
    

class demoattended(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile_Number=models.CharField(max_length=20)
    Courses=models.ForeignKey(Courses_Name,on_delete=models.CASCADE)
    Training=models.ForeignKey(Training,on_delete=models.CASCADE,null=True)
    Join = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')


class deleted(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile_Number=models.CharField(max_length=20)
    Courses=models.ForeignKey(Courses_Name,on_delete=models.CASCADE)
    Training=models.ForeignKey(Training,on_delete=models.CASCADE,null=True)


class Remove(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile_Number=models.CharField(max_length=20)
    Courses=models.ForeignKey(Courses_Name,on_delete=models.CASCADE)
    Training=models.ForeignKey(Training,on_delete=models.CASCADE,null=True)


class Demos(models.Model):
    Sno=models.IntegerField()
    Date=models.DateField()
    Course=models.ForeignKey(Courses_Name,on_delete=models.CASCADE)
    Faculty=models.CharField(max_length=30)
    Time=models.TimeField()
    Training=models.ForeignKey(Training,on_delete=models.CASCADE,null=True)




class Recent_Placed(models.Model):
    name=models.CharField(max_length=50,null=True)
    company=models.CharField(max_length=50,null=True)
    pakage=models.IntegerField(null=True)
    image=models.ImageField(upload_to='image/',null=True)
    course=models.ForeignKey(Courses_Name,on_delete=models.CASCADE ,null=True)

    def __str__(self):
        return self.name
    


# class Review(models.Model):
#     video = models.FileField(upload_to='videos/',null=True)
#     name=models.CharField(max_length=50,null=True)
    
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100,null=True)
    video = models.FileField(upload_to='videos/',null=True)
    # Add other fields as needed

    def __str__(self):
        return self.name


class Ourteam(models.Model):
    image=models.ImageField(upload_to='image/')
    name=models.CharField(max_length=30)
    description=models.TextField(null=True)


class Colabrations(models.Model):
    image=models.ImageField(upload_to='image/',null=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(null=True)
    mobile_number=models.CharField(max_length=12,null=True)
    admission_number = models.CharField(max_length=10,null=True)  # New field for admission number
    joining_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username
    
class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_date = models.DateField()
    marks = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"Test: {self.pk} - Student: {self.student.user.username}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance: {self.pk} - Student: {self.student.user.username}"


class Interview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    interview_date = models.DateField()
    present = models.BooleanField(default=False)
    performance = models.DecimalField(max_digits=4, decimal_places=2,validators=[MaxValueValidator(10)],null=True)
    marks=models.DecimalField(max_digits=8,decimal_places=2,validators=[MaxValueValidator(10)],null=True)

    def __str__(self):
        return f"Interview: {self.pk} - Student: {self.student.user.username}"
  

class StudentInquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    experience = models.CharField(max_length=20)
    experience_details = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=50)
    other_qualification = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=50)
    sub_course = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    ampm = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


    
    
