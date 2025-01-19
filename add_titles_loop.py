headers = []               #список заголовков
STOP_COMMAND = 'стоп'     #стоп слово
while True:               #запрашиваем у пользователя заголовки пока он не напишет стоп слово
    header = input("Введите заголовок заметки (или " + STOP_COMMAND + " для завершения): ")
    if header.lower() == STOP_COMMAND.lower(): # проверка на команду завершения
        break

    if header:
        headers.append(header)

print("Список заголовков заметок:")
for header in headers:
    print("- " + header)





