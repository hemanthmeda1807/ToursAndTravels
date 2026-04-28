from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
import stripe
try:
    from fpdf import FPDF
except ImportError:
    pass
from .models import Category, TourPackage, Booking, ContactMessage
from .forms import BookingForm, ContactForm, UserRegistrationForm

def home(request):
    featured_tours = TourPackage.objects.filter(featured=True)[:6]
    categories = Category.objects.all()
    return render(request, 'tours_app/home.html', {
        'featured_tours': featured_tours,
        'categories': categories
    })

def package_list(request):
    category_id = request.GET.get('category')
    if category_id:
        packages = TourPackage.objects.filter(category_id=category_id)
    else:
        packages = TourPackage.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'tours_app/package_list.html', {
        'packages': packages,
        'categories': categories
    })

def package_detail(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            if request.user.is_authenticated:
                booking.user = request.user
            booking.status = 'pending'
            booking.save()
            
            # Simulate Stripe checkout redirection
            return redirect('payment_simulation', booking_id=booking.id)
    else:
        form = BookingForm()
    
    return render(request, 'tours_app/package_detail.html', {
        'package': package,
        'form': form,
        'stripe_public_key': getattr(settings, 'STRIPE_PUBLIC_KEY', '')
    })

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message. We will get back to you shortly.")
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'tours_app/contact.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'tours_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'tours_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def profile(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    return render(request, 'tours_app/profile.html', {'bookings': user_bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, f"Your booking for {booking.package.title} has been cancelled.")
    else:
        messages.error(request, "This booking cannot be cancelled. Please contact support.")
    return redirect('profile')

@login_required
def payment_simulation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status != 'pending':
        return redirect('profile')
    return render(request, 'tours_app/payment_simulation.html', {'booking': booking})

@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'pending':
        booking.status = 'confirmed'
        booking.save()
        
        # Send email
        subject = f"Booking Confirmed: {booking.package.title}"
        message = f"Hi {booking.name},\n\nYour booking for {booking.package.title} on {booking.travel_date} has been confirmed.\n\nThank you for choosing AeroTravels!"
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@aerotravels.com')
        recipient_list = [booking.email]
        
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print("Failed to send email:", e)
            
        messages.success(request, "Payment successful! Your booking is confirmed.")
    return redirect('profile')

@login_required
def payment_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.error(request, "Payment was cancelled. Your booking is not confirmed.")
    return redirect('package_detail', pk=booking.package.pk)

@login_required
def download_ticket(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status != 'confirmed':
        messages.error(request, "Ticket is not available for this booking.")
        return redirect('profile')

    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('helvetica', 'B', 24)
    pdf.cell(0, 20, 'AeroTravels - Booking Ticket', align='C', new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font('helvetica', '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f'Booking ID: #{booking.id}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Name: {booking.name}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Package: {booking.package.title}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Location: {booking.package.location}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Travel Date: {booking.travel_date}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Travellers: {booking.travellers_count}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Total Price: ${booking.package.price * booking.travellers_count}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Status: {booking.status.upper()}', new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(20)
    pdf.set_font('helvetica', 'I', 10)
    pdf.cell(0, 10, 'Please present this ticket upon arrival.', align='C', new_x="LMARGIN", new_y="NEXT")
    
    response = HttpResponse(bytes(pdf.output()), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{booking.id}.pdf"'
    return response
