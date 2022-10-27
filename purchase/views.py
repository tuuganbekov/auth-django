from rest_framework import generics
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer
from generics import mixins


# Create your views here.
class PurchaseAPIView(
    generics.CreateAPIView
):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
