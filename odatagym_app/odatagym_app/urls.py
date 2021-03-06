"""odatagym_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from datasets_handler.views import DatasetsHandler
import examples.views as ex_views

from odatagym_app import settings

urlpatterns = [
    url(r'api/datasets/(?P<dataset_folder>[\w]+)/(?P<dataset_name>[\w-]+)/$',
        DatasetsHandler.as_view({'get': 'get'})),

    url(r'examples/sardinia_svg/', ex_views.get_sardinia_svg_example),
    url(r'examples/sardinia_drugstores/', ex_views.get_sardinia_drugstores),
    url(r'examples/rome_accidents/', ex_views.get_rome_accidents),

    url(r'^admin/', include(admin.site.urls)),
]
