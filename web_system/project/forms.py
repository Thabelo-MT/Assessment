from django.forms import ModelForm
from .models import TicketLogger

class TicketLoggerForm(ModelForm):
    class Meta:
        model = TicketLogger
        fields = '_all_'