from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError("You cannot select a past date for booking.")
        return selected_date
