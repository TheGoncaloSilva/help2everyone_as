from cProfile import label
from email.policy import default
from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterVol(forms.Form):
    email = forms.EmailField(label='Email')
    firstName = forms.CharField(label='First Name', max_length=50)
    lastName = forms.CharField(label='Last Name', max_length=50)
    phoneNumber = forms.IntegerField(label='Phone Number')
    ageOfBirth = forms.DateField(label='Birthdate', initial=datetime.date.today, widget = DateInput)
    image = forms.ImageField(label='Profile Image', required=False)
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    confirmPassword = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)

class RegisterOrg(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Company Name', max_length=100)
    image = forms.ImageField(label='Company Logo', required=False)
    contactNumber = forms.IntegerField(label='Contact Number')
    websiteAddress = forms.URLField(label='Website Address')
    foundationDate = forms.DateField(label='Foundation Date', initial=datetime.date.today, widget = DateInput)
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    confirmPassword = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
