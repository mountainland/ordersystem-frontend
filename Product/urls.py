from django.urls import path


from . import views


urlpatterns = (
    # urls for Product
    path('', views.ProductListView.as_view(), name='Product_order_create'),
    path('order/conformed/', views.order_conform, name='Product_order_conform'),
    path('order/create/', views.OrderCreateView.as_view(), name='Product_order_create'),

)