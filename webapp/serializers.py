from rest_framework import serializers
from .models import Product, Orders, Discount, About, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        product = Product
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    orders = ProductSerializer()

    class Meta:
        model = Orders
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    discount = OrdersSerializer(read_only=True)

    class Meta:
        model = Discount
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    blog = DiscountSerializer(read_only=True)

    class Meta:
        model = About
        fields = "__all__"




class ClientSerializer(serializers.ModelSerializer):
    country = DiscountSerializer(read_only=True)

    class Meta:
        model = About
        fields = "__all__"