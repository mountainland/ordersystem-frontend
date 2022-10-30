from django import forms
from .models import Product, Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['count'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control',})
        self.fields['postcode'].widget.attrs.update({'class': 'form-control',})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['information'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control'})
        self.fields['count'].widget.attrs['min'] = 1
        self.fields['count'].widget.attrs['max'] = 100
        self.fields['name'].label = "Nimi"
        self.fields['contact'].label = "Puhelinnumero"
        self.fields['count'].label = "Määrä"
        self.fields['address'].label = "Osoite"
        self.fields['postcode'].label = "Postinumero"
        self.fields['city'].label = 'Kaupunki'
        self.fields['information'].label = 'Lisätiedot'

    class Meta:
        model = Order
        fields = ['count_1', 'count_2', 'count_3', 'name','contact','address', 'postcode', 'city', 'information','payment_method',]