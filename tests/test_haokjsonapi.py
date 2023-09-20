# To run this test, run "pytest test_jsonapi.py" in terminal
import haokjsonapi

def test_complex():
    c = complex(1, 2)
    serialized = haokjsonapi.dumps(c)
    deserialized = haokjsonapi.loads(serialized)
    assert serialized == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
    assert type(deserialized) is complex

def test_range():
    r = range(1, 5, 2)
    serialized = haokjsonapi.dumps(r)
    deserialized = haokjsonapi.loads(serialized)
    assert serialized == '{"start": 1, "stop": 5, "step": 2, "__extended_json_type__": "range"}'
    assert type(deserialized) is range

def test_complex_and_range():
    my_data = {
        "hey": complex(1, 2),
        "there": range(1, 10, 3),
        73: False,
    }
    serialized = haokjsonapi.dumps(my_data)
    deserialized = haokjsonapi.loads(serialized)
    assert serialized == '{"hey": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "there": {"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}, "73": false}'
    assert type(deserialized) is dict
    assert type(deserialized["hey"]) is complex
    assert type(deserialized["there"]) is range
