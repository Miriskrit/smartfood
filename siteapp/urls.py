from django.urls import path

from . import views

urlpatterns = [
    # /siteapp/
    path('', views.IndexView.as_view(), name='index'),
    path('u/', views.UserInfoView.as_view(), name='info'),
    path('customvision/', views.BackgroundImageAnalyze.as_view(), name="customvision"),
    path('addfood/', views.BackgroundAddFoddView.as_view(), name="addfood"),
    path('foodanalize/', views.BackgroundFoodAnalzeView.as_view(), name="foodanalize"),
    path('faq/', views.FAQView.as_view(), name="faq")
]