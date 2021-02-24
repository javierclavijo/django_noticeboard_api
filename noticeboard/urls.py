from django.urls import path
from . import views

app_name = 'noticeboard'
urlpatterns = [
    path('', views.NoticeList.as_view(), name='all'),
    path('<int:pk>/', views.NoticeDetail.as_view(), name='detail')
    # path('expired/', views.ExpiredNoticeView.as_view(), name='expired-notices'),
    # path('<int:pk>/', views.SingleNoticeView.as_view(), name='single-notice'),
    # path('new/', views.NewNoticeView.as_view(), name='new'),
    # path('<int:pk>/delete', views.DeleteNoticeView.as_view(), name='delete'),
    # path('<int:pk>/update', views.UpdateNoticeView.as_view(), name='update')
]
