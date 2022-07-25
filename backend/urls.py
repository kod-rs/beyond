"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet, LoginView
    # BankViewSet, CarViewSet, JudgementView

from .api.startup import run_startup
run_startup()


router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
from django.http import JsonResponse

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)


from django.http import HttpResponse


from backend.api.view.dbView import pureDjangoView


urlpatterns = [

    # path('accounts/', include('allauth.urls')),

    # path('bank', BankViewSet.as_view, name='bank'),
    # path('car', CarViewSet.as_view, name='car'),
    # path('jud', JudgementView.as_view(), name='jud'),

    # path('auth/', include('social_django.urls', namespace='social')),

    path('puredjango', pureDjangoView, name='home'),

    # path('snippets/<int:pk>', views.snippet_detail),
    path('login/', LoginView.as_view()),

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

]


