from django import forms
from django.contrib.auth.models import User
from todoapp.models import todomodel

class UserregisterForm(forms.ModelForm):
    class  Meta:
           model=User
           #fields=__all__
           fields=["first_name","last_name","email","username","password"]
           #exclude=["is_user"]


class UserLoginForm(forms.ModelForm):
          class  Meta:
           model=User
           #fields=__all__
           fields=["username","password"]
           #exclude=["is_user"]
           widgets={
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.TextInput(attrs={'class':'form-control'}),

                
        } 
            


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=todomodel
        exclude=['user','status']
        widgets={
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.TextInput(attrs={'class':'form-control'}),

                
        } 


class TodoEditForm(forms.ModelForm):
    class Meta:
        model=todomodel
        exclude=['user']
        widgets={
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.TextInput(attrs={'class':'form-control'}),
                'status':forms.CheckboxInput(attrs={'class':'form-check-input'}),
                
        } 



        