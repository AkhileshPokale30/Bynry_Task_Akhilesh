# customer_service/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import CustomerProfile
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib import messages
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the customer profile
            CustomerProfile.objects.create(
                user=new_user,
                phone_number=request.POST.get('phone_number'),
                address=request.POST.get('address')
            )
            # Authenticate and login the user
            user = authenticate(username=new_user.username, password=user_form.cleaned_data['password'])
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'customer_service/register.html', {'user_form': user_form})



@login_required
def profile(request):
    return render(request, 'customer_service/profile.html')



@login_required
def dashboard(request):
    return render(request, 'customer_service/dashboard.html')




@login_required
def submit_service_request(request):
    customer = request.user.customer  # Assumes OneToOne relationship
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            messages.success(request, 'Your service request has been submitted successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_service_request.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Process form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'customer_service/login.html')

@login_required
def service_request_detail(request, pk):
    customer = request.user.customer
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=customer)
    return render(request, 'customer_service/service_request_detail.html', {'service_request': service_request})
