"""minitutorial URL Configuration

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
from django.urls import path
from bbs.views import hello, ArticleListView, ArticleDetailView, ArticleCreateUpdateView
urlpatterns = [
    path('hello/<to>', hello),
    path('admin/', admin.site.urls),
    path('article/', ArticleListView.as_view()),
    path('article/<input_id>', ArticleDetailView.as_view()),
    path('article/create/', ArticleCreateUpdateView.as_view()),
    path('article/<input_id>/update', ArticleCreateUpdateView.as_view()),
    path('article/<input_id>/delete', delete_content),
]
