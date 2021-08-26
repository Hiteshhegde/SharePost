from django import forms

#Create your forms here

#Login form
class LoginForm(forms.Form):
    user_name= forms.CharField(label='User name',max_length= 220)
    password = forms.CharField(label='Password',max_length=50)
    remember_me = forms.BooleanField(label='remember me ?')

#Registeration Form
class RegisterForm(forms.Form):
    user_name= forms.CharField(label='Username', max_length=220)
    password = forms.CharField(label='Password', max_length=50)
    email = forms.EmailField(label='Email') 
