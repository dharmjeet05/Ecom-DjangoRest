from rest_framework import viewsets

from .serializers import ProductSeralizer
from .models import Product

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSeralizer