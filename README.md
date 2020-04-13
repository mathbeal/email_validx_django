Description
-------------

Validx library defines new types like Str, Int, Dict. It helps validate a schema in a pleasant way.

The Email type is not defined. As I needed it with django, I subclass Str to create an Email schema.


Usage
-------

```python
schema = Dict({
    'name': Str(),
    'email': Email.schema(),
})

json_response = {
    'name': 'Toto',
    'email': 'toto@gmail.com',
}

schema(json_response)
```
