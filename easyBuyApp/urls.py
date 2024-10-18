from django.urls import path
from easyBuyApp import views

urlpatterns = [
    path('login',views.login_user,name="login"),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('',views.index,name='index'),
    path('productDetails/<int:id>',views.productDetails,name='productDetails'),
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('cards',views.cards,name="cards"),
    path('remove_card/<int:id>',views.remove_card,name="remove_card"),
    path('order/<int:id>',views.order,name="order"),
    path('showOrders',views.showOrders,name='showOrders'),
]