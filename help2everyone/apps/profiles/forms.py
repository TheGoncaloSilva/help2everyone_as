from cProfile import label
from email.policy import default
from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterEvent(forms.Form):
    eventMainImage = forms.ImageField(label='Foto de Capa', required=False)
    eventName = forms.CharField(label='Título', max_length=100)
    shortDescription = forms.CharField(label='Descrição pequena', max_length=90)
    description = forms.CharField(label='Descrição', max_length=1000, widget=forms.Textarea)
    totalVoluntarys = forms.IntegerField(label='Total Voluntaries')
    hours = forms.IntegerField(label='Horas Totais')
    address = forms.CharField(label='Endereço', max_length=200)
    zipCode = forms.CharField(label='Código Postal', max_length=8) # codigo postal
    district = forms.CharField(label='Distrito', max_length=100) # distrito  
    county = forms.CharField(label='Concelho', max_length=100) # concelho
    parish = forms.CharField(label='Freguesia', max_length=100) # freguesia
    country = forms.CharField(label='Pais', max_length=100) # pais
    startDate = forms.DateField(label='Data Início', initial=datetime.date.today, widget = DateInput)
    endDate = forms.DateField(label='Data Fim', initial=datetime.date.today, widget = DateInput)
    emailOrg = forms.EmailField(widget = forms.HiddenInput(), initial="ola@gmail.com")