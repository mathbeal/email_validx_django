from typing import Any, Dict, Optional

from django.core.exceptions import ValidationError  # type: ignore
from django.core.validators import EmailValidator as DjangoEmailValidator  # type: ignore
from validx import Str, exc


class Email(Str):

    def __init__(self, alias=None, replace=None,
                 validator=DjangoEmailValidator, **kw):
        """Email schema validation using EmailValidator from Django

        validator check that email has a valid format
        kw['pattern'] is secondary pattern email validation (ex: @compagny)
        """
        super(Email, self).__init__(alias=alias, replace=replace, **kw)
        self._validator = validator

    def __call__(self, value: Any) -> Any:
        """subclass __call__ to add validator checking.
        """
        value = super(Email, self).__call__(value)

        if self._validator:
            try:
                self._validator()(value)
            except ValidationError:
                raise exc.PatternMatchError(
                    expected='valid email',
                    actual=value,
                )
        return value
