from multiprocessing import context
from django.core.mail import send_mail
from .models import Name, Email, TicketID, DateLaunched, DateCompleted, TicketStatus
from .forms import CaptureGPS

# Capture the IP address of the user and store in the database.
def Index(request):
    context = {}
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward_for is not None:
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDRESS')
    print("IP Address of the user :", ip)