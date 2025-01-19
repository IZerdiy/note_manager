def main():
    statuses = ['выполнено', 'в процесе', 'отложено']  # доступные статусы
    current_status = 'в процессе'  #  текущий статус заметки
    print(current_status)
    while True:
        print('\nВозможные статусы: ')  # показываем список возможных статусов
        for status in statuses:
            print(f'{status}')
        new_status = input('введите новый статус:') # запрашиваем новый статус
        if new_status in statuses:
            current_status = new_status
            print(f'Статус обновлен на: {current_status} ') # статус обновлен на новый
            break
        else:
            print(f'Некорректный статус заметки. Пожалуйста, выберите статус из списка: {statuses}') # в случае если пользователь вводит не корректный статус
    print(f'\nОбновленный статус заметки: {current_status}')
if __name__ == '__main__':
    main()




