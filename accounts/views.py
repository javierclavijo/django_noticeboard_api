from django.shortcuts import render, get_object_or_404
from .forms import UserCreationExtendedForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from noticeboard.models import Notice


# Create your views here.
class RegistrationFormView(FormView):
    form_class = UserCreationExtendedForm
    template_name = 'registration/registration.html'
    success_url = 'done/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'registration/registration-success.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notices"] = Notice.objects.filter(
            author=self.object).order_by('-exp_date')
        return context


class CurrentUserProfileView(UserProfileView):
    success_url = reverse_lazy('noticeboard:active-notices')

    def get_success_url(self):
        return reverse_lazy('noticeboard:active-notices')

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
