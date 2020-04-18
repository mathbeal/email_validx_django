Description
-------------

Validx library defines new types like Str, Int, Dict. It helps validate a schema in a pleasant way.

The Email type is not defined. As I needed it with django, I subclass Str to create an Email schema.


Usage
-------

```python
schema = Dict({
    'name': Str(),
    'email': Email(),
})

valid_json = {
    'name': 'Toto',
    'email': 'toto@gmail.com',
}

invalid_json = {
    'name': 'Toto',
    'email': 'toto@@gmail.com',
}

schema(valid_json)  # json is valid, no exception raised.
schema(invalid_json)  # raise validx.exc.errors.PatternMatchError.
```
