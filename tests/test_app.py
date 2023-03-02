from app import app

def test_valid():
    assert app.valid('example@example.com', 'password') == True
    assert app.valid('notanemail', 'password') == False
    assert app.valid('example@example.com', 'wrongpassword') == False
