from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import ContactModel, Package
from .forms import TrackingForm

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Save to the database
            query = ContactModel(name=name, email=email, subject=subject, message=message)
            query.save()

            # Send email
            email_message = EmailMessage(
                subject=f"Email from {name}",
                body=f"User Email: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                to=['kingdavuchenna@gmail.com']
            )
            email_message.send(fail_silently=False)  # <-- show any error

            messages.success(request, "Your message has been sent successfully.")
            return redirect('/contact')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('/contact')

    return render(request, 'contact.html')


# Other views remain as they are
def home(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'index.html', {'form': form})

def track(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'track.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def services_details(request):
    return render(request, 'services_details.html')
