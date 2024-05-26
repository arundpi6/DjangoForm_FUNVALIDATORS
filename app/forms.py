from django import forms
from app.models import *


#VALIDATORS APPLYING FOR SUBMITTING DATAS -->

def validators_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('DONT START WITH A' )

def validators_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length must be 5' )



class TopicForm(forms.Form):
    Topic_Name=forms.CharField(validators=[validators_for_a,validators_for_len])


class WebpageForm(forms.Form):
    Topic_Name=forms.ModelChoiceField(queryset=Topic.objects.all())
    Name=forms.CharField(validators=[validators_for_a])
    URL=forms.URLField()
    Email=forms.EmailField()
