from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm): 
    email = forms.EmailField(required=True)

    class Meta: #fields that are to be shown in the registration form
        model = User
        fields = ('username','email','password1','password2')

    def save(self,commit=True): #overriding the default save() method in django.contrib.auth.forms
        user = super(UserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit: #commit variable is for consistency for now, may mean something ig we inherit this class
            user.save()
        return user
