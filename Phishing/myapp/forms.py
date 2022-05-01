from django import forms
# forms.py 
from .models import Black,UserRegister
class BlackForm(forms.ModelForm):
    class Meta:
        model=Black
        fields='__all__'
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields='__all__'