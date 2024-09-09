from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductView.as_view(),name="product" ),
    path("<int:productId>/", views.ProductEditView.as_view(),name="product_edit" ),
] 