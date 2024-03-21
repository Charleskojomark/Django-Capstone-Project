from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu', views.MenuItemsView.as_view(), name='menu'),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings', views.BookingView.as_view(), name='booking-list-create'),
]