from django import forms
from .models import Register
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['F_name','L_name','Email','Phone','DOB','Aadhar','GST','PAN','Passbook','Account','Ifsc']
        # fields = "__all__"
        # print(fields)

        widget = {
            'F_name': forms.TextInput(attrs={'placeholder': 'Email'}),
            'L_name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'Phone': forms.TextInput(attrs={'class':'form-control'}),
            'DOB': forms.DateInput(attrs={'class':'form-control'}),
            'Aadhar': forms.FileInput(attrs={'class':'form-control'}),
            'GST': forms.FileInput(attrs={'class':'form-control'}),
            'PAN': forms.FileInput(attrs={'class':'form-control'}),
            'Passbook': forms.FileInput(attrs={'class':'form-control'}),
            'Account': forms.TextInput(attrs={'class':'form-control'}),
            'Ifsc': forms.TextInput(attrs={'class':'form-control'}),
        }