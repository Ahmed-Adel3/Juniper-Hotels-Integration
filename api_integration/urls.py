from django.urls import path
from .views import (
    HotelPortfolio, HotelAvailability, HotelBookingRules,
    HotelBooking, HotelReadBooking, HotelCancelBooking, HotelBookingList)

urlpatterns = [
    path('hotel-portfolio/', HotelPortfolio.as_view()),
    path('hotel-availability/', HotelAvailability.as_view()),
    path('hotel-bookingrules/', HotelBookingRules.as_view()),
    path('hotel-booking/', HotelBooking.as_view()),
    path('hotel-readbooking/', HotelReadBooking.as_view()),
    path('hotel-cancelbooking/', HotelCancelBooking.as_view()),
    path('hotel-bookinglist/', HotelBookingList.as_view()),
]
