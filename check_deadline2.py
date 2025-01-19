import datetime

current_date = datetime.date.today() # Получение даты в данный момент
deadline = input('Введите дату дедлайна в формате ДД-ММ-ГГ: ') # Пользователь вводит дату дату дедлайна
try: # Оповещение в случае ввода неверного формата даты
    deadline_date = datetime.date(int(deadline.split('-')[2]), int(deadline.split('-')[1]), int(deadline.split('-')[0]))
except ValueError:
    print('Неверный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГ')
except IndexError:
    print('Неверный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГ')
if deadline_date < current_date: # Оповещает сколько осталось до дедлайна или когда он прошел
    print(f'Внимание! Дедлайн истек! {(current_date - deadline_date).days} дней назад')
elif current_date < deadline_date:
    print(f'Внимание! До дедлайна осталось {(deadline_date - current_date).days} дней')
else :
    print('Дедлайн наступил сегодня')

