from main import reverse

def test_reverse():
    test_data = ((42, None),
                 (['a','b','c'], None),
                 ('', ''),
                 ('a', 'a'),
                 ('aba', 'aba'),
                 ('abcd', 'dcba')
                 )
    for inp_s, out_s_correct in test_data:
        try:
            out_s = reverse(inp_s)
        except TypeError as E:
            if out_s_correct is None:
                continue
            if type(inp_s) == str:
                print(f'Error! reverse({inp_s}). Error:{E}')
            return False
        except Exception as E:
            if out_s_correct is None:
                continue
            if type(inp_s) == str:
                print(f'Error! reverse({inp_s}). Error:{E}')
            return False
        else:
            if out_s !=out_s_correct:
                print(f'Error! reverse({inp_s}) back {out_s} instead of {out_s_correct} ')
                return False
    print('all tests was successful')
    return True


if __name__ == '__main__':
    test_reverse()
