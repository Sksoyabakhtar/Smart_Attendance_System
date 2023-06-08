from socket import fromshare
from django import forms
from anonymous.models import UserProfileInfo
class UserProfileInfoForm(form.ModelForm):
    portfolio=forms.URLField(required=False)
    profile_pic=forms.ImageField(required=False)

    clas Meta():
    model=UserProfileInfo
    exclude=('user',)