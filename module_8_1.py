def add_everything_up(a,b):

    try:
        if isinstance(a and b, int): # ввел проверку для того, чтобы округлить ответ, иначе получалось 130.45600000000002
            return round((a + b), 3)
        else:
            return a + b
    except TypeError:
        return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('строка', 'яблоко'))

