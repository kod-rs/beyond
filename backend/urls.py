from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.api.views import LoginView, IndexView
from backend.api.startup import run_startup
run_startup()



router = routers.DefaultRouter()
# router.register('messages', MessageViewSet)

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)


from django.http import HttpResponse


from backend.api.view.dbView import pureDjangoView


urlpatterns = [

    # path('accounts/', include('allauth.urls')),

    # path('bank', BankViewSet.as_view, name='bank'),

    # path('auth/', include('social_django.urls', namespace='social')),

    path('puredjango', pureDjangoView, name='home'),

    # path('snippets/<int:pk>', views.snippet_detail),
    path('login/', LoginView.as_view()),
    path('', IndexView.as_view()),

    # http://localhost:8000/
    # path('', IndexView, name='index'),
    path('', IndexView.as_view()),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

]


