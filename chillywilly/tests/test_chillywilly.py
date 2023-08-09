import pytest
from chillywilly import Chillywilly, sample_function

@pytest.fixture
def Chillywilly_object():
    obj = Chillywilly()
    return obj

def test_Chillywilly_instance_has_sample_method(Chillywilly_object):
    assert hasattr(Chillywilly_object, "sample_method")

def test_chillywilly_has_sample_function():
    assert sample_function() is None  # no return value
