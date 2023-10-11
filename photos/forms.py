from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Album, Photo


class PhotoUploadForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('album', 'file')
        labels = {
            'album': '',
            'file': '',
        }
        widgets = {
            'album': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Album'}),
        }
    def __init__(self, *args, **kwargs):
        super(PhotoUploadForm, self).__init__(*args, **kwargs)

        self.fields['file'].widget.attrs['multiple'] = True

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'date', 'owner', 'description', 'users')
        labels = {
            'name': '',
            'date': 'YYYY-MM-MM HH:MM:SS',
            'owner': '',
            'description': '',
            'users': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Owner'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
            'users': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'users'}),
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'