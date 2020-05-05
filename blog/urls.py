from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('', views.login ,name='login'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('comment/', views.commnt_new ,name='commnt_new'),


]