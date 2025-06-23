# orders/forms.py

from django import forms
from .models import Order, Ticket
from django.forms import inlineformset_factory

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'status', 'comment']

TicketFormSet = inlineformset_factory(Order, Ticket, fields=('code', 'status', 'product_codes'), extra=1)
