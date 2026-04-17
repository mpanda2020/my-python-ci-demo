from app.main import add, get_env

def test_add():
    assert add(2, 3) == 5

def test_env():
    assert get_env() == "prod"