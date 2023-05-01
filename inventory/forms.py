from django import forms
from inventory.models import Item

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['category']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sample Item',
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sample Description',
                }
            ),
        }