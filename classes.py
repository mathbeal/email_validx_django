from validx import Dict, Str
from validx import exc

class Email:

    @staticmethod
    def schema(alias=None, replace=None, **kw):

        from django.core.validators import EmailValidator as DjangoEmailValidator
        from django.core.exceptions import ValidationError

        class EmailStr(Str):

            def __call__(self, value):
                value = super(EmailStr, self).__call__(value)
                try:
                    DjangoEmailValidator()(value)
                except ValidationError:
                    raise exc.PatternMatchError(expected='valid email',
                                                actual=value)
                return value
        return EmailStr(alias=alias, replace=replace, **kw)



if __name__ == '__main__':
    valid_sample = {
        'firstname': 'Toto',
        'lastname': 'titi',
        'email': 'toto.titi@gmail.com',
    }

    # invalid_sample = valid_sample.copy()    
    # invalid_sample['email'] = 12

    schema = Dict({
        'firstname': Str(),
        'lastname': Str(),
        'email': Email.schema(),
    })

    schema(valid_sample)
