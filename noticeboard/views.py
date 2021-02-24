from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsAuthorOrStaffMixin
from .models import Notice
from .forms import NewNoteForm
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.


class ActiveNoticesView(generic.ListView):
    def get_queryset(self):
        """Return only the notices which have not expired yet"""
        return Notice.objects.filter(exp_date__gt=timezone.now()).order_by('exp_date', 'title')
    model = Notice
    extra_context = {
        'title': 'Active Notices'
    }


class ExpiredNoticeView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        """Return only the notices which have expired"""
        return Notice.objects.filter(exp_date__lte=timezone.now()).order_by('-exp_date', 'title')
    model = Notice
    extra_context = {
        'title': 'Expired Notices'
    }


class SingleNoticeView(generic.DetailView):
    model = Notice


class NewNoticeView(LoginRequiredMixin, generic.CreateView):
    form_class = NewNoteForm
    template_name = 'noticeboard/notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteNoticeView(LoginRequiredMixin, UserIsAuthorOrStaffMixin, generic.DeleteView):
    model = Notice
    success_url = reverse_lazy('noticeboard:active-notices')


class UpdateNoticeView(LoginRequiredMixin, UserIsAuthorOrStaffMixin, generic.UpdateView):
    form_class = NewNoteForm
    model = Notice
    template_name = 'noticeboard/notice_form.html'
