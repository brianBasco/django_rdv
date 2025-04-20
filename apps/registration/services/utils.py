from django.forms import ValidationError
from django.http import HttpRequest
from django.contrib import messages
from django.core.validators import BaseValidator
from django.contrib.auth.password_validation import (MinimumLengthValidator,
                                                     NumericPasswordValidator)


def check_passwordValidation(request: HttpRequest, password: str):
    validators:list[BaseValidator] = [MinimumLengthValidator, NumericPasswordValidator]
    try:
        for validator in validators:
            validator().validate(password)
        return True
    except ValidationError as e:
        messages.add_message(request, messages.ERROR, str(e))
        return False