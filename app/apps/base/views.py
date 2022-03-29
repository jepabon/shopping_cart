from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as CoreLoginView

from apps.base.decorators import is_client


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"


class UserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LoginView(CoreLoginView):
    form_class = AuthenticationForm

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().dispatch(*args, **kwargs)

    def get_success_url(self):

        if self.request.user.is_authenticated:
            if self.request.GET.get('next'):
                return self.request.GET.get('next')
            if self.request.user.is_superuser:
                return reverse_lazy('admin:index')
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class SettingsView(TemplateView):
    template_name = "settings.html"