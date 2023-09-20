# jsonapi

`jsonapi` is a Python package that extends the built-in `json` library to support complex and range objects in JSON serialization and deserialization.

## Installation

You can install `jsonapi` using pip:

```bash
pip install jsonapi
```

## Usage

### Serializing Complex Objects

`jsonapi` allows you to serialize complex and range objects to JSON easily. To use it, import the `jsonapi` module and use the `dumps` function:

```python
import jsonapi

data = complex(1, 2)

json_str = jsonapi.dumps(data)
```

### Deserializing Complex Objects

You can also deserialize JSON data containing complex and range objects back into Python objects using `jsonapi`. Use the `loads` function:

```python
import jsonapi

json_str = '{"hey": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "there": {"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}, "73": false}'
data = jsonapi.loads(json_str)
```

## License

This package is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

We would like to thank the Python community and the creators of the `json` library for their valuable contributions.