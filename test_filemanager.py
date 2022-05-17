from use_functions import separate

def test_separate():
    assert separate('-', 10) == '----------'
    assert separate() == '********************'
