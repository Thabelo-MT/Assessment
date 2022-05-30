from django.shortcuts import render
from .forms import TicketLoggerForm

def index(request):
    form = TicketLoggerForm()
#Saving the personal details of the logger to the system
    if request.method == 'POST':
        form = TicketLoggerForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request, 'project/form.html', context)
#Capturing the GPS coordinates of the ticket logger
from django.core.mail import send_mail
