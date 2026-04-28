from django.contrib import admin
from .models import Category, TourPackage, Booking, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'price', 'duration_days', 'featured')
    list_filter = ('category', 'featured', 'location')
    search_fields = ('title', 'location', 'description')
    list_editable = ('featured', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'package', 'travel_date', 'travellers_count', 'status', 'booked_at')
    list_filter = ('status', 'travel_date')
    search_fields = ('name', 'email', 'package__title', 'user__username')
    readonly_fields = ('booked_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'received_at')
    readonly_fields = ('received_at',)
