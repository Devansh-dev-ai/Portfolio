from django import forms
from .models import ContactToUser,Owner,UserProjects


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactToUser
        fields = ['name', 'email', 'contact_phone', 'message']

class UserProjectsForm(forms.ModelForm):
    class Meta:
        model = UserProjects
        fields = ['name','description','github_link','project_picture']

# class UserResume(forms.ModelForm):
#     file = forms.FileField()
#     date_update = forms.DateTimeField()