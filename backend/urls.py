"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet, SnippetDetail

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)


from django.http import HttpResponse


def pureDjangoView(request):
    return HttpResponse("home page")


urlpatterns = [

    path('puredjango', pureDjangoView, name='home'),

    # path('snippets/<int:pk>', views.snippet_detail),
    path('login/', SnippetDetail.as_view()),

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

]


