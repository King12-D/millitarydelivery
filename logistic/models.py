from django.db import models
import uuid

# Package model for shipment tracking
class Package(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default="Unknown Address")
    receiver_email = models.EmailField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    location = models.CharField(max_length=100, default="Warehouse")  # New field for tracking location
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.receiver_name}"

# Contact model for storing contact form submissions
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name}'
