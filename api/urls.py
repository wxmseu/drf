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

from django.urls import path,re_path

from api.views import AuthView, OrderView,DjangoView,GroupView,UserView,RoleView

urlpatterns = [
    # api
    # path('auth/', AuthView.as_view()),
    # path('order/', OrderView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/order/$',OrderView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/order/(?P<id>[0-9]+)/$', OrderView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/auth/$', AuthView.as_view(),name='uuu'),
    re_path(r'^(?P<version>[v1|v2]+)/auth/(?P<id>[0-9]+)/$', AuthView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/django/$', DjangoView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/user/$', UserView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/group/(?P<xx>\d+)$', GroupView.as_view(),name='gp'),
    re_path(r'^(?P<version>[v1|v2]+)/role/$', RoleView.as_view()),

]
