from django import forms
from ads.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image_url', 'category', 'condition']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title',
                'class': 'font-secondary',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter product description',
                'rows': 5,
                'class': 'font-secondary',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Paste image URL (optional)',
                'class': 'font-secondary',
            }),
            'category': forms.Select(attrs={
                'class': 'font-secondary',
            }),
            'condition': forms.Select(attrs={
                'class': 'font-secondary',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
