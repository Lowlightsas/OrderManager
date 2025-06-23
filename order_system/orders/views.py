from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Order,Ticket
from .forms import OrderForm, TicketFormSet
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket,TICKET_STATUSES
from .serializers import TicketStatusUpdateSerializer
from .permissions import IsManager
from rest_framework.permissions import IsAuthenticated




def is_manager(user):
    if user.groups.filter(name='Managers').exists():
        return True
    raise PermissionDenied


def index(request):
    orders = Order.objects.order_by('-created_at')[:5]
    total_orders = Order.objects.count()
    total_customers = Order.objects.values_list('customer_name', flat=True).distinct().count()
    return render(request, 'temo/build/index.html', {'orders': orders, 'total_orders': total_orders, 'total_customers': total_customers})

@login_required
@user_passes_test(is_manager)
def tables(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'temo/build/pages/tables.html',{'orders': orders})


@login_required
@user_passes_test(is_manager)
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    tickets = order.tickets.all()
    return render(request, 'temo/build/pages/order_detail.html', {'order': order, 'tickets': tickets})


@login_required
@user_passes_test(is_manager)
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = TicketFormSet(request.POST, instance=order)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('orders:tables')
    else:
        form = OrderForm(instance=order)
        formset = TicketFormSet(instance=order)

    return render(request, 'temo/build/pages/edit.html', {
        'form': form,
        'formset': formset,
        'order': order  
    })



@login_required
@user_passes_test(is_manager)
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = TicketFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            formset.instance = order
            formset.save()
            return redirect('orders:order_detail', pk=order.pk)  
    else:
        form = OrderForm()
        formset = TicketFormSet()

    return render(request, 'temo/build/pages/add_order.html', {
        'form': form,
        'formset': formset,
    })


# API View для обновления статуса тикета

class UpdateTicketStatusAPI(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        new_status = request.data.get('status')

        if not code or not new_status:
            return Response({'error': 'code and status are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ticket = Ticket.objects.get(code=code)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)

        if new_status not in dict(TICKET_STATUSES):
            return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)

        ticket.status = new_status
        ticket.save()

        return Response({'message': f'Ticket {code} updated to {new_status}.'}, status=status.HTTP_200_OK)