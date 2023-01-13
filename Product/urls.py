from django.urls import path, include


from . import views


urlpatterns = (
    # urls for Product
    path('', views.ProductListView.as_view(), name='Product_order_create'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(),
         name='Product_product_detail'),
    # urls for order
    path('orders/', views.OrderListView.as_view(), name='Product_order_list'),
    path('orders/admin/', views.OrderAdminView.as_view(),
         name='Product_orders_admin'),
    path('order/conformed/', views.order_conform, name='Product_order_conform'),
    path('order/create/', views.OrderCreateView.as_view(),
         name='Product_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(),
         name='Product_order_detail'),
)
