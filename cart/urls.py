from django.contrib import admin
from django.urls import path
from cart import views


urlpatterns = [
    path('add-to-cart/<int:i>/', views.AddToCartView.as_view(), name='addtocart'),
    
    path('cart/', views.CartView.as_view(), name='cartview'),
    
    path('removecart/<int:i>', views.DecrementCartView.as_view(), name='minuscart'),
    path('incriment/<int:i>/',views.Increment_cart.as_view(),name="pluscart"),
    path('deleteproduct/<int:i>', views.DeleteProduct.as_view(), name='deletproduct'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('paymentsuccess/', views.Paymentsuccess.as_view(), name='paymentsuccess'),
    path('orderdetail/', views.OrderDetailView.as_view(), name='orderdetail'),
]