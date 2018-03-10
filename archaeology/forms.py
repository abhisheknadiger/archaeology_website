from django import forms
from .models import *

class MusuemForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    class Meta:
        model = Museum
        fields = ['name','location','desc','opening_time','closing_time','holiday','photo']
        widgets = {
            'opening_time':forms.TimeInput(attrs={'type':'time'}),
            'closing_time':forms.TimeInput(attrs={'type': 'time'}),
        }



class MonumentForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    class Meta:
        model = Monument
        fields = ['name','location','desc','opening_time','closing_time','holiday','photo']
        widgets = {
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ArtifactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    class Meta:
        model = Artifact
        fields = '__all__'


class MessageForm(forms.ModelForm):
    name = forms.CharField(required=True)
    class Meta:
        model = message
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    name = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    working_on = forms.CharField(required=True)
    class Meta:
        model = Projects
        fields = ['name','date','desc','working_on']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class LibraryForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    class Meta:
        model = Library
        fields = '__all__'

class ExcavationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    photo = forms.ImageField(required=True)
    class Meta:
        model = Excavations
        fields = '__all__'
        widgets = {
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User_profile
        fields = ['name','email','username','password','contact_no']


class PublicationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    class Meta:
        model = Publication
        fields = ['name','paper','Abstract','desc']

    def clean(self):
        cleaned_data = super(PublicationForm, self).clean()

        name = cleaned_data.get('name')
        if name == None:
            raise forms.ValidationError("Please enter the name")


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = feedback
        fields = [ 'rating' , 'text' ]

    def clean(self):
        cleaned_data = super(FeedbackForm,self).clean()
        rating = cleaned_data.get('rating')
        text = cleaned_data.get('text')
        if rating > 5 and rating <1:
            raise forms.ValidationError("Invalid rating")
        if rating == None or text == None:
            raise forms.ValidationError("Please enter some text")
        if text == "" or text == None:
            raise forms.ValidationError("Please enter feedback")

class ArtifactFeedbackForm(forms.ModelForm):

    class Meta:
        model = artifact_feedback
        fields = [ 'rating' , 'text' ]

    def clean(self):
        cleaned_data = super(ArtifactFeedbackForm,self).clean()

        rating = cleaned_data.get('rating')
        if rating > 5 and rating <1:
            raise forms.ValidationError("Invalid rating")
        text = cleaned_data.get('text')
        if text == "":
            raise forms.ValidationError("Please enter feedback")
class MuseumFeedbackForm(forms.ModelForm):

    class Meta:
        model = museum_feedback
        fields = [ 'rating' , 'text' ]

    def clean(self):
        cleaned_data = super(MuseumFeedbackForm,self).clean()

        rating = cleaned_data.get('rating')
        if rating > 5 and rating <1:
            raise forms.ValidationError("Invalid rating")
        text = cleaned_data.get('text')
        if text == "":
            raise forms.ValidationError("Please enter feedback")

class ticketform(forms.ModelForm):
    class Meta:
        model = Buy_ticket
        fields = ['adult_no','child_no']

    def clean(self):

        cleaned_data = super(ticketform, self).clean()
        adult_no = cleaned_data.get('adult_no')
        child_no = cleaned_data.get('child_no')
        print (adult_no)
        if adult_no < 0 or child_no <0:
            raise forms.ValidationError("Please enter correct values")
        elif not (adult_no > 0 or child_no > 0):
            raise forms.ValidationError("Please enter the number of People")
        elif not (adult_no > 0):
            raise forms.ValidationError("There should be one adult ")


class MuseumTicketForm(forms.ModelForm):
    class Meta:
        model = Buy_museum_ticket
        fields = ['adult_no','child_no']

    def clean(self):

        cleaned_data = super(MuseumTicketForm, self).clean()
        adult_no = cleaned_data.get('adult_no')
        child_no = cleaned_data.get('child_no')
        print (adult_no)
        if adult_no < 0 or child_no <0:
            raise forms.ValidationError("Please enter correct values")
        elif not (adult_no > 0 or child_no > 0):
            raise forms.ValidationError("Please enter the number of People")
        elif not (adult_no > 0):
            raise forms.ValidationError("There should be one adult ")

class ExcavationTicketForm(forms.ModelForm):
    class Meta:
        model = Buy_excavation_ticket
        fields = ['adult_no','child_no']

    def clean(self):

        cleaned_data = super(ExcavationTicketForm, self).clean()
        adult_no = cleaned_data.get('adult_no')
        child_no = cleaned_data.get('child_no')
        print (adult_no)
        if adult_no < 0 or child_no <0:
            raise forms.ValidationError("Please enter correct values")
        elif not (adult_no > 0 or child_no > 0):
            raise forms.ValidationError("Please enter the number of People")
        elif not (adult_no > 0):
            raise forms.ValidationError("There should be one adult ")