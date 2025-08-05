from main import add # importing the add function from a file named main.py

def test_add():
    assert add(2, 3) == 5 # if it is giving 5 or not
    assert add(0, 0) == 0
