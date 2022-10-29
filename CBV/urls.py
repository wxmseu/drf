"""CBV URL Configuration

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
from django.urls import path, include, re_path
from book.views import BookView
from sers.views import Book  # ,BookDetailView

# 路由组件
from rest_framework import routers

# 文档路由
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('sers/book', Book)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/', views.book),
    # path('book/', views.BookView.as_view()),
    # path('book/', BookView.as_view()),
    # path('sers/book/', Book.as_view()),
    # path('sers/book/<int:pk>', BookDetailView.as_view()),
    # path('sers/book/', Book.as_view(all)),
    # re_path(r'sers/book/(?P<id>\d+)', Book.as_view(one)),
    path('docs/', include_docs_urls(title='站点页面标题')),

    # api
    path('api/', include('api.urls')),
]
urlpatterns += router.urls
