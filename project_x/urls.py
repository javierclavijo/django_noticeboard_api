from django.urls import include, path
from rest_framework.routers import DefaultRouter

from noticeboard.views import NoticeViewSet
from users.views import UserViewSet

"""project_x URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notices', NoticeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
