"""fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
import goods.urls
import user.urls
import message.urls
import order.urls
import cart.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(goods.urls),name='goods'),#商品
    path('user/', include(user.urls),name='user'),#用户
    path('message/', include(message.urls),name='message'),#消息
    path('order/', include(order.urls),name='order'),#订单
    path('cart/', include(cart.urls),name='cart'),#购物车
]
