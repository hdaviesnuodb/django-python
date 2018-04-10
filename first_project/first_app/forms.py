from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


#Add custom validators
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with a Z')

class FormName(forms.Form):
    #name=forms.CharField(validators=[check_for_z])
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email again: ")
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super(FormName,self).clean();
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure emails match')


    #Using django validators
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # This is the way if not using django validator
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput)
    #
    # def clean_botcatcher(self):
    #     botcacher = self.cleaned_data['botcatcher']
    #     if len(botcacher) > 0:
    #         raise forms.ValidationError("Gotcha Bot")
    #     return botcacher
