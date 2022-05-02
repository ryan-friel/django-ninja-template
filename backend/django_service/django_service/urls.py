from django.contrib import admin
from django.urls import path
from gainful.api import api as gainful_api
from gainful import views as gainful_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", gainful_api.urls),
    path("", gainful_views.index, name='gainful_index')
]