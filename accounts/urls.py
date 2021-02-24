from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             extra_context={'title': 'Log in'}
         ),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='registration/logout.html'
         ),
         name='logout'),
    path('registration/',
         views.RegistrationFormView.as_view(
             extra_context={'title': 'Sign in'}
         ),
         name='registration'),
    path('registration/done/',
         views.RegistrationSuccessView.as_view()),
    path('<int:pk>/',
         views.UserProfileView.as_view(),
         name='user-profile'),
    path('my/',
         views.CurrentUserProfileView.as_view(),
         name='current-user'),
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='home'),
]
