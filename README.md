# haokjsonapi

`haokjsonapi` is a Python package that extends the built-in `json` library to support complex and range objects in JSON serialization and deserialization.

## Installation

You can install `haokjsonapi` using pip:

```bash
pip install haokjsonapi
```

## Usage

### Serializing Complex Objects

`haokjsonapi` allows you to serialize complex and range objects to JSON easily. To use it, import the `haokjsonapi` module and use the `dumps` function:

```python
import haokjsonapi

data = complex(1, 2)

json_str = haokjsonapi.dumps(data)
```

### Deserializing Complex Objects

You can also deserialize JSON data containing complex and range objects back into Python objects using `haokjsonapi`. Use the `loads` function:

```python
import haokjsonapi

json_str = '{"hey": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "there": {"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}, "73": false}'
data = haokjsonapi.loads(json_str)
```

## License

This package is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

We would like to thank the Python community and the creators of the `json` library for their valuable contributions.