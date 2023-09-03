from django import forms

class MyForm(forms.Form):
    OPTIONS = (
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('hospitality', 'Hospitality'),
    )

    selected_options = forms.MultipleChoiceField(
        choices=OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Set to True if at least one option must be selected
    )
