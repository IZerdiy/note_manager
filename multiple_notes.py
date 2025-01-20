from datetime import datetime



title_list = []

def create_note():

    try:  # Оповещение в случае ввода неверного формата даты
            current_date = datetime.today()
            name = input("Введите имя: ")
            title = input("Введите заголовок: ")
            description = input("Введите описание: ")
            status = input("Введите статус ('в процессе' 'новая', 'завершено'): ")
            if status != 'в процессе' and status != 'новая' and status != 'завершено':
                 raise Exception('статус неверный')
            creation_date = input("Введите дату создания (формат: ДД-ММ-ГГГГ): ")
            creation_date = datetime.strptime(creation_date, "%d-%m-%Y")
            deadline = input('Введите дату дедлайна в формате ДД-ММ-ГГ: ')
            deadline = datetime.strptime(deadline, "%d-%m-%Y")
            if deadline < current_date:  # Оповещает сколько осталось до дедлайна или когда он прошел
                    print(f'Внимание! Дедлайн истек! {(current_date - deadline).days} дней назад')
            elif current_date < deadline:
                    print(f'Внимание! До дедлайна осталось {(deadline - current_date).days} дней')
            else:
                    print('Дедлайн наступил сегодня')
            return {
                    "name": name,
                    "title": title,
                    "description": description,
                    "status": status,
                    "creation_date": creation_date,
                    "deadline": deadline
                }
    except ValueError:
            print('Неверный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГ')
    except Exception as e:
         print(e)
def add_note_to_list(notes):
    new_note = create_note()
    notes.append(new_note)
    return notes
def main():
    notes = []
    while True:
        add_new_note = input('добавить новую заметку да/нет: ')
        if add_new_note.lower() == 'да':
            notes = add_note_to_list(notes)
        elif add_new_note.lower() == 'нет':
            break
        elif add_new_note.lower() == 'стоп':
            break
        else:
            print('Некорректный воод. Попробуйте снова')
if __name__ == '__main__':
    main()
