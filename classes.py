from typing import Any

from django.core.exceptions import ValidationError  # type: ignore
from django.core.validators import EmailValidator as DjangoEmailValidator  # type: ignore
from validx import Str, exc


class Email(Str):

    def __init__(self, *args, email_validator=DjangoEmailValidator, **kwargs):
        super(Email, self).__init__(*args, **kwargs)

        self.email_validator = email_validator

    def __call__(self, value: Any, __context=None) -> Any:
        """subclass __call__ to add validator checking.
        """
        value = super(Email, self).__call__(
            value,
            __context=__context,
        )

        if self.email_validator:
            try:
                self.email_validator()(value)
            except ValidationError:
                raise exc.PatternMatchError(
                    expected='valid email',
                    actual=value,
                )

        return value
