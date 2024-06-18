from django.urls import path
from .views import LandingPageView, OrdersView, UserRegisterView, UsersLoginView, ProductListView, DiscountsView, AboutView, ClientView
urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("order/", OrdersView.as_view(), name="order"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("shop/", ProductListView.as_view(), name="shop"),
    path("discount/", DiscountsView.as_view(), name="discount"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ClientView.as_view(), name="contact"),
    path("login/", UsersLoginView.as_view(), name="login"),

]