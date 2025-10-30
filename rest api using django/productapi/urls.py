from django.urls import path
from productapi.views import ProductAPIListCreateView

urlpatterns = [
  # Define your API endpoints here
    path('products/', ProductAPIListCreateView.as_view(), name='product-list-create'),
]