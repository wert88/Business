from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login

class IndexView(View):
	def get(self, request):
		return render(request, 'main/index.html')

class AboutUs(View):
	def get(self, request):
		return render(request, 'main/about.html')

class Gallery(View):
	def get(self, request):
		pics = Picture.objects.all()
		return render(request, 'main/index.html', {'pics':pics})

class UserFormView(View):
    form_class = UserForm
    template_name = 'main/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})