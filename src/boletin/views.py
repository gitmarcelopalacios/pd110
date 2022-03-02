import abc
import email
from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

# Create your views here.
def inicio(request):
    _titulo="Bienvenido"
  
    #if request.user.is_authenticated(self, authuri)
    if request.user.is_authenticated:
        _titulo = "Bienvenido %s" %(request.user)
    else:
        _titulo = "Bienvenido Usuario Anónimo"
    
    _form=RegModelForm(request.POST or None)

    context =  {
        "ctx_titulo": _titulo,
        "ctx_form": _form,
    }
    if _form.is_valid():
        instance = _form.save(commit=False)
        if not instance.nombre:
            instance.nombre = "Persona desconocida"
        instance.save()

        context =  {
            "ctx_titulo": "Gracias %s!" %(instance.nombre),
        }
        
        if not instance.nombre:
            context =  {
                "ctx_titulo": "Gracias %s!" %(instance.email),
            }
            
        
        print(instance)
        print(instance.timestamp)
        
        
        
        # form_data = _form.cleaned_data

        # _nombre = form_data.get("nombre")
        # _email = form_data.get("email")
        
        #  alternativa 1 
        # obj = Registrado.objects.create(email=abc)
        
        # alternativa 2
        # obj = Registrado()
        # obj.email = _email
        # obj.nombre = _nombre
        # obj.save()

        #  alternativa 3 
        # obj = Registrado.objects.create(email=_email, nombre=_nombre)


    return render(request, "inicio.html", context)

def Contact(request):
    form=ContactForm (request.POST or None) 
    if form.is_valid():
        
        # for key, value in form.clean_data.items():
        #     print(key, value)

        for key in form.cleaned_data:
            print(key)
            print(form.cleaned_data.get(key))

        # email=form.cleaned_data.get("email")
        # mensaje=form.cleaned_data.get("mensaje")
        # nombre=form.cleaned_data.get("nombre")
        #print(email,mensaje,nombre)
    context={
        "form": form,
    }    
    return render(request, "forms.html", context)
    