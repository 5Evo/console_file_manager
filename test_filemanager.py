from use_functions import separate, add_separators

def test_separate():
    assert separate('-', 10) == '----------'
    assert separate() == '********************'


