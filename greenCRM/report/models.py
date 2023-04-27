from django.contrib.auth.models import User
from django.db import models
from client.models import Client

class Report(models.Model):
    name = models.CharField(max_length=225, default='unknown')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reports')
    org_name = models.CharField(max_length=225, default='unknown')
    state = models.CharField(max_length=100, default='unknown')
    total_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    customer_type = models.CharField(max_length=20, choices=(('restaurant', 'Restaurant'), ('store', 'Store')), default='unknown')
    created_by = models.ForeignKey(User, related_name='reports', on_delete = models.CASCADE)
    sales_rep = models.ForeignKey(Client, related_name='reports_sales', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Get values from related client object
        self.org_name = self.client.org_name
        self.state = self.client.state
        self.total_order_value = self.client.total_order_value
        self.customer_type = self.client.customer_type
        super(Report, self).save(*args, **kwargs)