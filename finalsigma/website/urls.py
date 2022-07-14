from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register_request, name="register"),
  path('login/', views.login_request, name='login'),
  path('logout/', views.logout_request, name="logout"),
]
