from warnings import warn

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator as DjangoEmailValidator
from validx import Str, exc


class Email:

    @staticmethod
    def schema(alias=None, replace=None, **kw):

        kw_copy = dict(kw)

        if kw_copy.get('pattern', None) is not None:
            warn(
                f"pattern is ignored, use Str(pattern={kw['pattern']}, ...) instead"
            )
            del kw_copy['pattern']

        class EmailStr(Str):

            def __call__(self, value):
                value = super(EmailStr, self).__call__(value)

                try:
                    DjangoEmailValidator()(value)
                except ValidationError:
                    raise exc.PatternMatchError(expected='valid email',
                                                actual=value)
                return value

        return EmailStr(alias=alias, replace=replace, **kw_copy)
