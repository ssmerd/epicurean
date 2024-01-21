from django.shortcuts import render
from django.contrib import messages
from django.views import generic    
from django.urls import reverse_lazy
from .forms import BookTableForm, DivErrorList, UserForm
from .utils import print_parameters
from .helper import BookingHelper

def index(request):
    """ Main view """
    
    if request.method == "POST":
        form = BookTableForm(request.POST, error_class=DivErrorList)
    else:
        form = BookTableForm()

    if request.method == "POST":
        if form.is_valid():

            # Debugging parameters 
            print_parameters(form)
            
            booking_helper = BookingHelper(form)

            if booking_helper.save_booking():
                messages.success(request, "Your booking was successful.")
            else:
                messages.success(request, "There is no table left.")

            form = BookTableForm()

    return render(request, 'home.html', {"form": form})


class SignUpView(generic.CreateView):
    """" Signup view """
    form_class = UserForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
