from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.package_list, name='package_list'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    path('contact/', views.contact_us, name='contact_us'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('booking/<int:booking_id>/payment/simulate/', views.payment_simulation, name='payment_simulation'),
    path('booking/<int:booking_id>/payment/success/', views.payment_success, name='payment_success'),
    path('booking/<int:booking_id>/payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('booking/<int:booking_id>/ticket/', views.download_ticket, name='download_ticket'),
]
