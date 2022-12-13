"""website1 URL Configuration

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

urlpatterns = [
    # admin page, can be used to manage website insides, to get to this page  type http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # default page if you type just http://127.0.0.1:8000
    path('', include('page1.urls', namespace='page1')),
    # page of app1, if you type http://127.0.0.1:8000/page1
    path('hello/', include('page1.urls', namespace='page1')),
    # add another page from index file
    path('page2/', include('page2.urls', namespace='page2')),
    # and one more page
    path('page3/', include('page3.urls', namespace='page3'))
]
