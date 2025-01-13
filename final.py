Name = input('Имя: ')
status = input('статус: ')
title = input('Заголовок: ')
subtitle1 = input('Подзаголовок_1: ')
subtitle2 = input('Подзаголовок_2: ')
content = input('Содержание: ')
created_date = input('Дата создания в формате ДД.ММ.ГГ')
note = [Name, status, [title, subtitle1, subtitle2], content, created_date]
print('Список заголовков: ', note)