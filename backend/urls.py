from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.api.views import IndexView
from backend.api.view.loginView import LoginView
from backend.api.view.logoutView import LogoutView
from backend.api.view.deviceView import DeviceView
from backend.api.startup import run_startup
run_startup()

api_router = routers.DefaultRouter()
api_router.register('device', DeviceView, basename="device")

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)


from django.http import HttpResponse


from backend.api.view.dbView import pureDjangoView
from backend.api.model.testCRUD import TestCrudView
from backend.api.model.locationsView import LocationsView

urlpatterns = [
    path('', IndexView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path("device/<int:pk>", DeviceView.as_view()),
    path("device/", DeviceView.as_view()),

    # path('accounts/', include('allauth.urls')),

    # path('bank', BankViewSet.as_view, name='bank'),

    # path('auth/', include('social_django.urls', namespace='social')),

    path('puredjango', pureDjangoView, name='home'),

    # path('snippets/<int:pk>', views.snippet_detail),
    path('', IndexView.as_view()),

    path("testcrud/", TestCrudView.as_view()),

    path("locations/", LocationsView.as_view()),

    # http://localhost:8000/
    # path('', IndexView, name='index'),


    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(api_router.urls)),

    path('api/admin/', admin.site.urls),

]


