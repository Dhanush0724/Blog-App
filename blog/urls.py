from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns  = [
    path('login/',views.loginPage,name="login"),
    path('',views.index,name='blog-index'),
    path('logout/',views.logoutUser,name="logout"),
    
    path('register/',views.registerPage,name="register"),

    path('profile/',views.profilePage,name="profile"),

    path('about/',views.out,name="out"),
    path('contact/',views.contact,name="contact"),

    path('savecontact/',views.savecontact,name='savecontact'),

    
    path('post-details/<int:pk>/',views.post_detail,name='blog-post-details'),
    path('post_edit/<int:pk>/',views.post_edit,name='blog-post-edit'),
    path('post_delete/<int:pk>/',views.post_delete,name='blog-post-delete'),  

    path('search/', views.search,name='search'),

    
   path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]