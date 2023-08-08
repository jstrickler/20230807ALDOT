def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4, "reality is broken"   # if assert statement succeeds, the test passes

def test_spam():
    print("spam test", end=" ")  # debugging only
    assert "parts" is "parts"
