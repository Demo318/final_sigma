from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
  path('', views.index, name='index'),
  path('post/<slug:post_title_slug>/', views.show_post, name='show_post'),
  path('register/', views.register_request, name="register"),
  path('login/', views.login_request, name='login'),
  path('logout/', views.logout_request, name="logout"),
]
