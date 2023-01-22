from django import forms
from .models.contact_model import ContactModel
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = ContactModel
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "message",
        )
        labels = {
            "first_name": "Emri",
            "last_name": "Mbiemri",
            "phone_no": "Numri i telefonit",
            "message": "Mesazhi",
        }
