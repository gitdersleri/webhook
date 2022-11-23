"""git URL Configuration

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
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):

    def post(self,request):
        data = request.data
        print("DATA: ",data)
        return Response(data)

class HelloView(APIView):
    def get(self,request):
        return Response({"message":"Hello world"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("github/",TestView.as_view(),name="test_view"),
    path("",HelloView.as_view(),name="hello_view")
]
