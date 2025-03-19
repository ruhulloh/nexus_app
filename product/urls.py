
from django.urls import path
from .views import category_products, product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', category_products, name='product-list'),
    path('detail/<int:pk>/', product_detail, name='product-detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
