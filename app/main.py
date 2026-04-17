import os

def add(a, b):
    env = os.getenv("APP_ENV", "dev")
    return a + b

def get_env():
    return os.getenv("APP_ENV")