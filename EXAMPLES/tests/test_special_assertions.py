import pytest
import math

FILE_NAME = 'IDONOTEXIST.txt'

# import from "real" code
def read_file(file_name: str) -> str:
    f = open(file_name)
    return f.read() 


def test_missing_filename():
    with pytest.raises(FileNotFoundError):  # assert FileNotFoundError is raised inside block
        read_file(FILE_NAME)  # will fail test if file is not found

def test_pytest_approx():
    print()
    assert (.1 + .2) == pytest.approx(.3)  # fail unless values are within 0.000001 of each other (actual result is 0.30000000000000004)

def test_approximate_pi():
    assert 22 / 7 == pytest.approx(math.pi, .001)  # Default tolerance is 0.000001; smaller (or larger) tolerance can be specified

