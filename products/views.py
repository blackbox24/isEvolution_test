from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ModelViewSet 

from .models import Product,User
from .serializers import ProductSerializer
from .permissions import IsOwner
# Create your views here.
    
class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,IsOwner)
