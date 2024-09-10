from.models import  Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model= Product
        fields=('id',
                'title',
                'seller_username',
                'content',
                'created_at',
                'updated_at',
                'image',
                )
