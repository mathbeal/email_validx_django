import pytest
from validx import Dict
from validx.exc import ValidationError

from .classes import Email

valid_emails = [
    'toto@gmail.com',
    'toto.tata@gmail.com',
    'toto_t@gmail.com',
    'toto123@gmail.com',
]

company_valid_emails = list(
    map(
        lambda x: f"{x}@mycompany.com",
        ['denise.sabrina'
         'marc.sanders',
         'marketing_service',
         'jean.dupont32'],
    ),
)

invalid_emails = [
    '',
    'toto@@gmail.com',
    '.toto@gmail.com',
    'toto..@gmail.com',
    '..toto@gmail.com',
    'toto..tata@gmail.com',
    '.@gmail.com',
    '@',
    '@gmail.com',
    '123@gm',
]


@pytest.mark.parametrize("email", valid_emails)
@pytest.mark.parametrize("minlen", [None, 1])
@pytest.mark.parametrize("maxlen", [None, max(map(len, valid_emails))])
def test_valid_email(email, minlen, maxlen):
    schema = Email(minlen=minlen, maxlen=maxlen)
    try:
        schema(email)
    except Exception as error:
        pytest.fail(
            f'{email}:{min}:{max} is not valid email as expected, {error}'
        )


@pytest.mark.parametrize("email", invalid_emails)
@pytest.mark.parametrize("minlen", [None, 1 + max(map(len, valid_emails))])
@pytest.mark.parametrize("maxlen", [None])
def test_invalid_email(email, minlen, maxlen):
    schema = Email(minlen=minlen, maxlen=maxlen)
    with pytest.raises(ValidationError):
        schema(email)


@pytest.mark.parametrize("email", company_valid_emails)
@pytest.mark.parametrize("pattern", [r".*@mycompany.com"])
def test_valid_email_with_valid_pattern(email, pattern):
    schema = Email(pattern=pattern)
    try:
        schema(email)
    except Exception as error:
        pytest.fail(f'{email} is not valid email as expected, {error}')


@pytest.mark.parametrize("email", company_valid_emails)
@pytest.mark.parametrize("pattern", [r".*@myCOMpany.com", ])
def test_valid_email_with_invalid_pattern(email, pattern):
    with pytest.raises(ValidationError):
        schema = Email(pattern=pattern)
        schema(email)


@pytest.mark.parametrize('email', company_valid_emails)
@pytest.mark.parametrize('pattern', [r".*@mycompany.com$"])
def test_validx_dict_with_valid_email(email, pattern):

    schema = Dict({
        'email': Email(pattern=pattern),
    })

    try:
        schema({'email': email})
    except Exception as error:
        pytest.fail(
            f'{email} is not valid email as expected, {error}',
        )
