from django import forms

from .models import Estate, Realtor, Branch


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = [
            'title',
            'location',
            'documents',
            # 'image',
            'landmarks',
            'features',
            'price',
            'discounted_price',
            'image',
            'subscription_form',
            'google_map',
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'documents':forms.TextInput(attrs={'class':'form-control'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'}),
            'landmarks':forms.TextInput(attrs={'class':'form-control'}),
            'features':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'discounted_price':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'subscription_form':forms.FileInput(attrs={'class':'form-control'}),
            'google_map':forms.TextInput(attrs={'class':'form-control'})
            
        }

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = [
            'name',
            'address',
            # 'image',
            'contact',
            'email',
            'gender',
            'state',
            'profile_picture',
            'invite',
            'account_number',
            'account_name',
            'bank_name',
            'receipt'
        ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'profile_picture':forms.FileInput(attrs={'class':'form-control'}),
            'invite':forms.TextInput(attrs={'class':'form-control'}),
            'account_number':forms.TextInput(attrs={'class':'form-control'}),
            'account_name':forms.TextInput(attrs={'class':'form-control'}),
            'bank_name':forms.TextInput(attrs={'class':'form-control'}),
            'receipt':forms.FileInput(attrs={'class':'form-control'}),
            
        }

