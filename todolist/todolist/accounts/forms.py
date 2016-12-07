from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'user_permissions')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name == '':
            raise forms.ValidationError('Este campo e obrigatorio')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name == '':
            raise forms.ValidationError('Este campo e obrigatorio')
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Este campo e obrigatorio')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email ja existente.')
        return email
