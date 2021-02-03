from django import forms
from api.models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ProductrForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['F_name','L_name','Email','Phone','DOB','Aadhar','GST','PAN','Passbook','Account','Ifsc']


        # widget = {
        #     'product_name': 
        # }