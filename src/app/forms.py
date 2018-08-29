from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']
        
    def clean_password_confirmation(self):
        print(self.cleaned_data)
        pass0 = self.cleaned_data.get('password')
        pass1 = self.cleaned_data.get('password_confirmation')
        if pass0 != pass1:
            raise forms.ValidationError("The password confirmation must match the password.")
        return pass0
