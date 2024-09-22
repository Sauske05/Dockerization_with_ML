from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('predict/', views.generate_model_val, name='predict'),
]