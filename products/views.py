from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from api.mixin import StaffEditorPermissionMixin

# Create your views here.

# get a product


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# post a product


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
            serializer.save(content=content)
        return super().perform_create(serializer)

# post a product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListCreateAPIView(
        StaffEditorPermissionMixin,
        generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
