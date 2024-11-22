# urls.py
from django.urls import path
from .views import ProductsByDivision,ProductDetails,CalculateLotDetails
from .addtocart import AddToCart,CartDetailsView
from .Custlogin import CustomerauthLoginView
from .placeorder import PlaceOrder



urlpatterns = [
    path('get-products-by-division/', ProductsByDivision.as_view(), name='get-products-by-division'),
    path('get-products-details/', ProductDetails.as_view(), name='get-products-details'),
    path('calculate-margin/', CalculateLotDetails.as_view(), name='calculate-margin'),
    path('addto-cart/', AddToCart.as_view(), name='addto-cart'),
    path('cart-details/', CartDetailsView.as_view(), name='cart-details'),
    path('customer/login/', CustomerauthLoginView.as_view(), name='customer_login'),
    path('placeorder/', PlaceOrder.as_view(), name='placeorder'),






]
    