from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import Product
from.serializer import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    
class ProductView(APIView):
    #post일 때만 로그인 필수
    def permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    #post일 때, 새 글 작성
    def post(self, request):
        errors=[]

        for field in ['title', 'image', 'content']:
            if request.data.get(field) is None :
                errors.append(f"{field}는 필수입니다.")

        if len(request.data.get('title')) > 50:
            errors.append("title은 50자를 넘을 수 없습니다.")
            
        if errors:
            return Response({"errors": errors}, status=400)

        product=Product.objects.create(
            title=request.data.get('title'),
            content=request.data.get('content'),
            image=request.data.get('image'),
            seller = request.user
            )
        return Response(f"{product.title}이 생성되었습니다.", status=201)
    
    #get일때 상품 목록조회
    pagination_class = ProductPagination

    def get(self, request):
        products = Product.objects.all()
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)