from django import forms
from .models import BarterRequest, Ad




class BarterRequestForm(forms.ModelForm):
    ad_sender = forms.ModelChoiceField(
        queryset=Ad.objects.none(),
        label="Choose your ad to offer",
        widget=forms.Select(attrs={"class": "font-secondary"})
    )

    comment = forms.CharField(
        label="Comment",
        required=False,
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Optional message...",
            "class": "font-secondary"
        })
    )

    class Meta:
        model = BarterRequest
        fields = ["ad_sender", "comment"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["ad_sender"].queryset = Ad.objects.filter(user=user)