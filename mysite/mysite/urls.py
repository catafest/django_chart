"""mysite URL Configuration

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
from django.urls import path
from test001.views import home_page
from test001.views import Test001ChartView
# add Post to urls.py 
from test001.views import posts
#
from django.urls import include, path
from rest_framework import routers
from test001 import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = 'test001'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_page, name ='home'),
    path('', Test001ChartView.as_view(), name = 'home'), 
    path('posts/',posts, name = 'posts'),
    # Use automatic URL routing
    # Can also include login URLs for the browsable API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
