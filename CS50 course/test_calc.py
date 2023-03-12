import pytest
from calcuator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


#--------------------------------------------- this works too so I can test multiple categories(functions) so it gives me errors after the first error if there is one

def test_postive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")



    
    

   