from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db import models
from django.conf import settings
from django_extensions.db import fields as extension_fields
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from Payment.models import Payment_method
from City.models import City


class Product(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ('category', '-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_product_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_product_update', args=(self.slug,))

class Order(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=5)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    count_1 = models.IntegerField(default=0, null=True, blank=True)
    product_1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Order.product_1+", null=True, blank=True) #57
    count_2 = models.IntegerField(default=0, null=True, blank=True)
    product_2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Order.product_2+", null=True, blank=True) #57
    count_3 = models.IntegerField(default=0, null=True, blank=True)
    product_3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Order.product_3+", null=True, blank=True) #FIXME #57
    cost = models.IntegerField(default=0, null=True, blank=True)
    information = models.CharField(max_length=500, null=True,blank=True)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(blank=True, null=True)
    # Relationship Fields
    
    order_by = CurrentUserField(blank=True, null=True, related_name="orders_user", on_delete=models.CASCADE)

    class Meta:
        ordering = ('delivered','-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_order_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_order_update', args=(self.slug,))


    def save(self, *args, **kwargs):
        if self.delivered:
            if not self.delivered_on:
                self.delivered_on = timezone.now()
        super(Order, self).save(*args, **kwargs)

