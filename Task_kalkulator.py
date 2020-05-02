while True:
    one = int(input('Введите число: '))
    two = input('Введите сложение(+,-,*,/): ')
    three = int(input('Введите число: '))
    if two == '+':
        four = one + three
        print(four)
        
    elif two == "-":
        four = one - three
        print(four)
        
    elif two == '*':
        four = one * three
        print(four)
        
    elif two == "/":
        three == 0
        print('На ноль делить дельзя!!!')
        continue
        four = one / three
        print(four)