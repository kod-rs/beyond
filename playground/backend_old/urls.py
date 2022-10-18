"""template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from rest_framework import routers

from playground.backend_old.api.comm.json_loader import role_validation_cfg
from playground.backend_old.api.startup import startup_configuration
from playground.backend_old.api.view.indexView import IndexView

startup_configuration.init_scheme_validator(role_validation_cfg)
startup_configuration.print_app_logo()

api_router = routers.DefaultRouter()
# api_router.register('device', DeviceView, basename="device")

# router.register('tmp', TmpViewSet)
# router.register('snippets/<int:pk>', SnippetDetail)

urlpatterns = [
    path('', IndexView.as_view()),

    # path("settings/", SettingsView.as_view()),
    #
    # path('login/', LoginView.as_view()),
    #
    # path('logout/', LogoutView.as_view()),
    #
    # path("colour/", ColourView.as_view()),
    # path("colour/<str:name>", ColourView.as_view()),
    #
    # path("location/<str:portfolio>", LocationView.as_view()),
    # path("location/<str:portfolio>/<str:name>", LocationView.as_view()),
    # path("location/<str:portfolio>/<str:section>/<str:_type>",
    #      LocationView.as_view()),
    # # path("location/<str:pn>", LocationsView.as_view()),
    # path("location/", LocationView.as_view()),
    #
    # path('api/admin/', admin.site.urls),
    #
    # path("csrf/", CSRFView.as_view()),
    #
    # path("consumption/<str:portfolio>/<str:section>/<str:_type>",
    #      ConsumptionView.as_view()),
    # path("consumption/<str:portfolio>/<str:section>/<str:_type>/<str:options>",
    #      ConsumptionView.as_view()),
    # path("consumption/", ConsumptionView.as_view()),
    # # todo add resolver for float
    # path("consumption/<str:value>", ConsumptionView.as_view()),
    #
    # path("portfolio/", PortfolioView.as_view()),
    # path("portfolio/<str:name>", PortfolioView.as_view())

]
