from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.UserFormView.as_view(), name='signup'),
	path('about_us/', views.AboutUs.as_view(), name='about'),
	path('gallery/', views.Gallery.as_view(), name='gallery'),
	path('contact_us/', views.ContactUs.as_view(), name='contact_us'),
]
