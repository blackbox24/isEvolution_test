from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from rest_framework import urls as rest_framework_urls

schema = get_schema_view(
    openapi.Info(
        title="IsEvloution Product CRUD API",
        default_version="1.0.0",
        description="Product API with CRUD commands",
    ),
    public=True,
    permission_classes = (AllowAny,)
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest_framework/",include(rest_framework_urls)),
    path("api/products/",include("products.urls")),
    path("api/docs/",schema.with_ui("swagger",cache_timeout=0),name="swagger")
]
