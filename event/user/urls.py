from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.signIn, name='login'),
    path('profile/', views.profile, name='profile_page'),
    path('logout/', views.logout_view, name='logout_page'),
]