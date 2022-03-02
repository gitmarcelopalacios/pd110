from dataclasses import fields
from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    
    class Meta:
        model=Registrado
        fields  = ("nombre", "email")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")        
        if not "cine.com" in proveedor:
            raise forms.ValidationError("El proveedor de correo debe ser cine.com")
        return email
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #validaciones
        return nombre
    
class ContactForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)   
    
  