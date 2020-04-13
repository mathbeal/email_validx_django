import pytest
from validx.exc import ValidationError
from .classes import Email

valid_emails = ['toto@gmail.com',
                'toto.tata@gmail.com',
                'toto_t@gmail.com',
                'toto123@gmail.com']

invalid_emails = ['',
                  'toto@@gmail.com',
                  '.toto@gmail.com',
                  'toto..@gmail.com',
                  '..toto@gmail.com',
                  'toto..tata@gmail.com',
                  '.@gmail.com',
                  '@',
                  '@gmail.com',
                  '123@gm']


@pytest.mark.parametrize("email", valid_emails)
@pytest.mark.parametrize("minlen", [None, 1])
@pytest.mark.parametrize("maxlen", [None, max(map(len, valid_emails))])
def test_valid_email(email, minlen, maxlen):
    schema = Email.schema(minlen=minlen, maxlen=maxlen)
    try:
        schema(email)
    except Exception as error:
        pytest.fail(f'{email} is not valid email as expected, {error}')

        
@pytest.mark.parametrize("email", invalid_emails)
@pytest.mark.parametrize("minlen", [None, 1 + max(map(len, valid_emails))])
@pytest.mark.parametrize("maxlen", [None])
def test_invalid_email(email, minlen, maxlen):
    schema = Email.schema(minlen=minlen, maxlen=maxlen)
    with pytest.raises(ValidationError):
        schema(email)

        
@pytest.mark.parametrize("email", valid_emails)
@pytest.mark.parametrize("pattern", [r"^[a-z0-9\.]+",])
def test_invalid_pattern_with_valid_email(email, pattern):
    with pytest.warns(Warning) as record:
        schema = Email.schema(pattern=pattern)
        schema(email)
        if not record:
            pytest.fail('Expecting a pattern warning')
