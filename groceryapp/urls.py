from django.urls import path,include
from. import views
# from .views import ReactPageView


urlpatterns = [
    path('',views.index,name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contactus/', views.contactus, name='contactus'),
    path('gallery/', views.gallery, name='gallery'),
    path('shopdetails/', views.shopdetails, name='shopdetails'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('our-location/', views.Location, name='our-locaion'),
    path('sign-in/', views.Signin, name='sign-in'),
    path('register/', views.Register, name='register'),
    path('signup/', views.Signup, name='sign-up'),
    path('Api/',views.user_data, name='Api'),
    path('Login/', views.Login_view, name='Login'),
    # path("account/", ReactPageView.as_view(), name='myaccount'),
    path('account/',views.react_view, name='myaccount'), 
    
    

]
