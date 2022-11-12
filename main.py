def reverse(s):
    if type(s) != str:
        raise TypeError(f"Ожидается строчный тип, получен тип {type(s)}")
    return s[::-1]