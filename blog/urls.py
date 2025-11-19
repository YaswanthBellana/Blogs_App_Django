"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('db-check/', blog_views.db_connection_check),
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('create/', blog_views.create_post, name='create_post'),
    path('edit/<int:pk>/', blog_views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', blog_views.delete_post, name='delete_post'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', blog_views.register, name='register'),
    path('sql/', blog_views.execute_raw_sql, name='execute_raw_sql'),
    path('error/404/', blog_views.custom_404_view, name='custom_404'),
    path('error/500/', blog_views.custom_500_view, name='custom_500'),
]
