from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from django.urls import reverse_lazy

from .forms import UserRegistrationForm, UserLoginForm


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/auth_page.html'
    extra_context = {"title": "Login"}

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_active:
                messages.error(request, 'Your account is inactive. Please contact support.')
                return redirect('login')
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)


class LogoutUser(LogoutView):
    def get_success_url(self):
        return reverse_lazy('main')


class RegisterView(View):
    template = 'accounts/auth_page.html'

    form_class = UserRegistrationForm

    def get(self, request):
        data = {
            'title': 'Create an Account',
            'form': self.form_class()
        }
        return render(request, self.template, data)

    def post(self, request):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main')
        data = {
            'title': 'Create an Account',
            'form': self.form_class()
        }
        return render(request, self.template, data)