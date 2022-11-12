def reverse(s):
    if type(s) != str:
        raise TypeError(f"Ожидается строчный тип, получен тип {type(s)}")
    return s[::-1]

def test_reverse():
    assert reverse('abc') == 'cba'

def test_empty():
    assert reverse('') == ''

def test_polindrom():
    assert reverse('aba') == 'aba'

def test_one_sym():
    assert reverse('a') == 'a'