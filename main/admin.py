from django.contrib import admin
from .models import Picture, Contact
from .forms import ContactForm

admin.site.register(Picture)
admin.site.register(Contact)
