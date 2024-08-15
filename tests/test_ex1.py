import pytest

def test_example():
    print("test1")
    assert 1==1
    
@pytest.mark.skip
def test_example2():
    assert 1==1