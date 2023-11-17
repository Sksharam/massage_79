from django.urls import path
from massage_app import views

urlpatterns = [
    path('create',views.create),
   # path('dashboard',views.dashboard)
]
  