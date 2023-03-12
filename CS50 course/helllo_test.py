from helllo import hello


def test_helllo():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

