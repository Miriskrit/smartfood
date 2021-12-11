from django.urls import path

from . import views

urlpatterns = [
    # /siteapp/
    path('', views.IndexView.as_view(), name='index'),
    path('u/', views.UserInfoView.as_view(), name='info'),
    path('customvision/', views.BackgroundImageAnalyze.as_view(), name="customvision"),
    path('add/', views.BackgroundAddView.as_view(), name="add")
]