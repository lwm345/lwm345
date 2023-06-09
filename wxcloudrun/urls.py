"""wxcloudrun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include

from wxcloudrun import views
from django.conf.urls import url
from login import views as login_view
from user import views as user_view

urlpatterns = (
    # 计数器接口
    url(r'^^api/count(/)?$', views.counter),

    # 获取主页
    url(r'^^(/)?$', views.index),

    url(r"login/", login_view.login),
    url(r"user/", include('user.urls')),
)
