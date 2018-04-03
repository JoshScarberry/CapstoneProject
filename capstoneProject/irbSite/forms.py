#from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Project


class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #custom label for field
        self.fields['username'].label = 'User Name'
        #self.fields['email'].label = 'Email Address'

class IndexForm(ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', )

#class ProjectForm1(ModelForm):
#    class Meta();
#    model = Project
#    fields = ()
