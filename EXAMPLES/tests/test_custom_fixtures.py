import pytest

class Spam():
    def get_five(self):
        return 5

@pytest.fixture
def spam():
    """
    Instance of Spam
    """
    return Spam()

@pytest.fixture
def colors():
    """
    A list of colors
    """
    return ['pink', 'orange', 'purple', 'green']

@pytest.fixture
def before_after():
    """
    Value 100 with setup and teardown
    """
    print("\n******* BEFORE! *******")  # setup -- before test runs
    yield 100
    print("\n"
          "******* AFTER! *******")  # teardown -- after test runs

def test_get_five_returns_five(spam):
    assert spam.get_five() == 5

def test_spam_has_get_five_method(spam):
    assert hasattr(spam, "get_five")

def test_some_color_is_pink(colors):
    assert any(color == 'pink' for color in colors)

@pytest.mark.beforeafter
def test_beforeafter(before_after, colors):
    assert before_after == 100
    assert 'green' in colors

def test_temp_dir1(tmpdir):
    print("TEMP DIR:", str(tmpdir))
    assert 1

def test_temp_dir2(tmpdir):
    print("TEMP DIR:", str(tmpdir))
    assert 1

def test_temp_dir3(tmpdir):
    print("TEMP DIR:", str(tmpdir))
    assert 1

def test_temp_dir4(tmpdir):
    print("TEMP DIR:", str(tmpdir))
    assert 1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])