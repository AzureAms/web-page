"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from article_template import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('AzureAms/', include('article_template.urls')),
    path('admin/', admin.site.urls),
    path('index.html', views.index, name='index.html'),
    path('view_article', views.view_article, name='view article'),
    path('article/<int:order>', views.article_page, name="article_page"),
    path('news.html', views.view_all_article, name="All article"),
]
