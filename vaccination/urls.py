from django.urls import path
from . import views
# URLConf
urlpatterns = [
    path("covid19/", views.covid19_description, name="covid19"),
]