from django import forms
from . models import *
class NewStudentForm(forms.ModelForm):
    class Meta:
        model=newstudent
        fields='__all__'

class TrainingForm(forms.ModelForm):
    class Meta:
        model=Training
        fields='__all__'

class DemosForm(forms.ModelForm):
    class Meta:
        model=Demos
        fields='__all__'

class OurteamForm(forms.ModelForm):
    class Meta:
        model=Ourteam
        fields='__all__'

class ColabrationsForm(forms.ModelForm):
    class Meta:
        model=Colabrations
        fields='__all__'

class Recent_PlacedForm(forms.ModelForm):
    class Meta:
        model=Recent_Placed
        fields='__all__'

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=Review
#         fields='__all__'
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'video']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

from django import forms
from .models import StudentInquiry

class StudentInquiryForm(forms.ModelForm):
    class Meta:
        model = StudentInquiry
        fields='__all__'  # Specify any fields to exclude here



