from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        label='Your Name'
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput,
        label='Your Email Address',
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Message',
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.captcha_valid = kwargs.pop('captcha_valid', None)

        super(ContactForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.captcha_valid:
            raise(forms.ValidationError('Please prove you\'re not part of the Borg!'))

        return self.cleaned_data