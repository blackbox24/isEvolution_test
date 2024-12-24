from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

route = DefaultRouter()
route.register(r"",ProductView,basename="product-api")

urlpatterns = route.urls
# urlpatterns = [
#     path("",ProductListView.as_view(),name="product-list"),
#     path("create/",ProductCreateView.as_view(),name="product-create"),
#     path("delete/<int:pk>/",ProductDeleteView.as_view(),name="product-delete"),
#     path("update/<int:pk>/",ProductUpdateView.as_view(),name="product-update"),
# ]