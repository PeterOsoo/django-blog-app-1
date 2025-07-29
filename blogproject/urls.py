"""
URL configuration for blogproject project.

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
from django.urls import path, include

from django.conf.urls import handler404, handler500
from pages import views as pages_views  # Assuming you use 'pages' app



urlpatterns = [
    path('', include('pages.urls')),  # 👈 homepage & static pages
    path('admin/', admin.site.urls),
     path('blog/', include('blog.html_urls')),  # 👉 HTML views for blog
    path('api/', include('blog.api_urls')),    # 👉 API-only endpoints
    path('auth/', include('accounts.urls')),  # 👈 This line

]


# Custom error handlers
handler404 = 'pages.views.custom_404'
handler500 = 'pages.views.custom_500'
handler400 = 'pages.views.custom_400'
handler403 = 'pages.views.custom_403'
