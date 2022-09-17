users = {
      'Asan': {
            'phone' : '+996500123456',
            'name' : 'Asan',
            'cash' : 10000,
            'password' : '12345'
            },
      'Ulan2002' : {
            'phone' : '+996500123456',
            'name' : 'Usan',
            'cash' : 10000,
            'password' : '12345'
            },
      }   
key = None
while True:
    print('Здраствуйте уважаемый клиент!')
    m = int(input('''
    1 Зарегистрироваться 
    2 Авторизоваться 
    3 Перевод баланса 
    4 Информация 
    5 Выход аккаунта
    6 Выход
    >>> '''))
    if m == 1:
        if key is None:
            login = input('введите логин>>> ')
            name = input('введите полное ваше имя>>> ')
            phone = int(input('введите ваш номер +996'))
            password = input('Придумайте пароль>>> ')
            password1 = input('Подтвердите пароль>>> ')
            while password != password1 and len(password) < 8:
                password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
                password1 = input('Повторите пароль>>> ')
            
            else:
                print('Регистрация прошла успешно!\n')
                key = login
                users.update({
                    login :{
                        'name':name,
                        'phone':phone,
                        'cash':1000,
                        'password':password,
                    }
                })
    
    elif m == 2:    
        if key is None:
            print('Добро пожаловать в авторизацию ')
            login = input('Введите логин>>> ')
            password = input('введите пароль>>> ')
            if login in users:
                if password == users[login]['password']:
                    key = login
                    if key is not None:
                        print('Вы авторизовались ')
                    else:
                        print('Не корекное авторизация')
                else:
                    print('Не верный пароль')
            else:
                print('Нет такого пользователя ')
        else:
            print('Вы уже авторизованы ')
    
    elif m == 3:
        if users is not None:
            loginP = input('Введите имя получателя>>> ')
            summa = int(input('введите сумму перевода>>> '))
            if loginP in users:
                if summa <= users[key]['cash']:
                    users[key]['cash'] -= summa
                    users[loginP]['cash']+= summa
                    print('Перевод успешен')
                else:
                    print('У вас не достаточно денег')
            else:
                print('Такого пользователя нет')
        else:
            print('Вы не авторизованы')
    
    elif m == 4:
        if key is not None:
            print(f'''name = {users[login]['name']}
            login = {users}
            phone = {users[login]['phone']}
            cash = {users[login]['cash']}''')
        else:
            print('Вы не автотизированы')
    
    elif m == 5:
        users.pop(login)
        print(f'{login} удален')
    
    elif m == 6:
        print('Вы вышли!')
        break
    else:
        print('Убедитесь что ввели правильно!')
    