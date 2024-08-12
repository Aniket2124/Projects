from django.urls import path
from blog import views
urlpatterns = [
    path('', views.view_all_post, name='all_posts'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
    path('register/', views.register, name='register'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.User_profile, name='profile'),
]