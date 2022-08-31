from django.urls import path
from cookies import views

urlpatterns = [
    path('cookies/', views.CookiesView.as_view()),
]