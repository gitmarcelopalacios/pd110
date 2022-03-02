from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado 

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["nombre","email","timestamp"]
    form=RegModelForm
    list_filter = ["nombre","email","timestamp"]
    list_display_links = ["nombre"]
    list_editable = ["email"]
    search_fields = ["nombre","email"]
    # class Meta:
    #     model = Registrado

admin.site.register(Registrado, AdminRegistrado)
