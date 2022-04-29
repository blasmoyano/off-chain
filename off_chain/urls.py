"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Urls
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Off Chain API",
        default_version="v1",
        description="Documentation for API Off Chain",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("balance.urls")),
    url(
        r"api/v1/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

admin.site.site_header = "Off Chain"
admin.site.index_title = "Administrador"
admin.site.site_title = "Ripio - Off Chain"
