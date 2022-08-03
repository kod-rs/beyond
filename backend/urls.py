from django.contrib import admin
from django.urls import path
from rest_framework import routers

from backend.api.model.testCRUD import TestCrudView
from backend.api.startup import run_startup
from backend.api.view.dbView import pureDjangoView
from backend.api.view.deviceView import DeviceView
from backend.api.view.locationsView import LocationsView
from backend.api.view.loginView import LoginView
from backend.api.view.logoutView import LogoutView
from backend.api.views import IndexView

run_startup()

api_router = routers.DefaultRouter()
api_router.register('device', DeviceView, basename="device")

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)

urlpatterns = [
    path('', IndexView.as_view()),

    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path("device/<int:pk>", DeviceView.as_view()),
    path("device/", DeviceView.as_view()),

    path('puredjango', pureDjangoView, name='home'),

    path("testcrud/", TestCrudView.as_view()),

    path("locations/<int:pk>", LocationsView.as_view()),
    path("locations/", LocationsView.as_view()),

    path('api/admin/', admin.site.urls),

    # path('accounts/', include('allauth.urls')),
    # path('bank', BankViewSet.as_view, name='bank'),
    # path('auth/', include('social_django.urls', namespace='social')),
    # path('snippets/<int:pk>', views.snippet_detail),
    # http://localhost:8000/
    # path('', IndexView, name='index'),
    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(api_router.urls)),

]
