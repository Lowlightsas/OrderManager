from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'orders'


urlpatterns = [
    path('',views.index,name='index'),
    path('tables/',views.tables,name='tables'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('edit/<int:pk>/', views.order_edit, name='order_edit'),
    path('create/', views.order_create, name='order_create'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/tickets/update_status/',views.UpdateTicketStatusAPI.as_view(), name='update_ticket_status'),
]
