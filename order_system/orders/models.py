from django.db import models
from django.contrib.auth.models import User

ORDER_STATUSES = [
    ('new','Новый'),
    ('processing','В обработке'),
    ('done','Завершен'),
]

TICKET_STATUSES = [
    ('pending','Ожидает'),
    ('in_progress','В работе'),
    ('completed','Завершен'),
]

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20,choices=ORDER_STATUSES,default='new')
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer_name}"
    
class Ticket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tickets')
    code = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=TICKET_STATUSES, default='pending')
    # JSON-поле для хранения списка кодов товаров
    product_codes = models.JSONField(help_text="Список кодов товаров, например ['abc123', 'def456']")


    def __str__(self):
        return f"Тикет {self.code} (заказ #{self.order.id})"