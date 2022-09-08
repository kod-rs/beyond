from django.contrib import admin
from django.urls import path
from rest_framework import routers

from backend.api.view.locationsView import LocationsView
from backend.api.view.loginView import LoginView
from backend.api.view.logoutView import LogoutView
from backend.api.view.indexView import IndexView
from backend.api.view.CSRFView import CSRFView
from backend.api.view.portfolioView import PortfolioView
from backend.api.view.colourView import ColourView

from backend.api.comm.json_loader import role_validation_cfg

from backend.api.startup import startup_configuration
startup_configuration.init_scheme_validator(role_validation_cfg)
startup_configuration.print_app_logo()



api_router = routers.DefaultRouter()
# api_router.register('device', DeviceView, basename="device")

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)

urlpatterns = [
    path('', IndexView.as_view()),

    path('login/', LoginView.as_view()),

    path('logout/', LogoutView.as_view()),

    path("colour/", ColourView.as_view()),
    path("colour/<str:abc>", ColourView.as_view()),

    path("locations/<str:pn>", LocationsView.as_view()),
    path("locations/", LocationsView.as_view()),

    path('api/admin/', admin.site.urls),

    path("csrf/", CSRFView.as_view()),

    path("portfolio/", PortfolioView.as_view()),
    path("portfolio/<str:name>", PortfolioView.as_view()),

    #
    # path("locations/<int:pk>", LocationsView.as_view()),
    # path("device/<int:pk>", DeviceView.as_view()),

    # path('puredjango', pureDjangoView, name='home'),


    # path('accounts/', include('allauth.urls')),
    # path('bank', BankViewSet.as_view, name='bank'),
    # path('auth/', include('social_django.urls', namespace='social')),
    # path('snippets/<int:pk>', views.snippet_detail),
    # http://localhost:8000/
    # path('', IndexView, name='index'),
    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(api_router.urls)),

]
