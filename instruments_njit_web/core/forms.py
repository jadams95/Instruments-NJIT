from django import forms

class CheckoutForm(forms.Form):
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    shipped = forms.BooleanField(required=False)
    credit_card_number = forms.CharField(max_length=16)
    expiration_date = forms.DateField()
    cvv = forms.CharField(max_length=4)
