from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class MobileValidator(RegexValidator):
    regex = r'09(\d{9})$'
    message = _("Enter a valid mobile number")
