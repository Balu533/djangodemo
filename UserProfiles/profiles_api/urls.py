from django.urls import path
from . import views


urlpatterns = [

    path('api_view/', views.HelloApiView.as_view()),

]
