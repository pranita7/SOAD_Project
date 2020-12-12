from django import forms

from donate.models import Donate_Post


class DonatePostCreateForm(forms.ModelForm):
    class Meta:
        model = Donate_Post
        fields = {
            'title',
            'body',
            'doorNo',
            'residence',
            'street',
            'city',
            'state',
            'country',
            'pinCode',
            'image',
            'availableitems',
        }

class DonatePostEditForm(forms.ModelForm):
    class Meta:
        model = Donate_Post
        fields = {
            'title',
            'body',
            'doorNo',
            'residence',
            'street',
            'city',
            'state',
            'country',
            'pinCode',
            'image',
            'availableitems',
        }


class AddressForm(forms.Form):
    your_doorNo = forms.CharField(max_length=20)
    your_residence = forms.CharField(max_length=40)
    your_street = forms.CharField(max_length=40)
    your_country = forms.CharField(max_length=20)
    your_pinCode = forms.IntegerField()
    your_address = forms.CharField(label='City/town', max_length=100)
    your_state = forms.CharField(label='State', max_length=100)