def display_page(notes, page):
    start_index = 0 + page *5
    end_index = 5 + page *5
    
    for index, note in enumerate(notes[start_index:end_index], start=1):
        print(f"""
        Заметка: {index},
        Имя пользователя: {note['username']},
        Заголовок: {note['title']}
        Описание: {note['content']}
        Дата создания: {note['date_created']}
        Дедлайн: {note['issue_date']},
        """)
        print('-' *50) 
   
def display_notes(notes, puge_number = 0):
    if len(notes) == 0:
        print('У вас нет сохранённых заметок.!')
    else:
       display_page(notes, puge_number)

if __name__ == '__main__':
    notes = [
        {"username": "1", "title": "Y", "status": "F"},
        {"username": "2", "title": "список покупок", "content": "купить покупки на неделю", "date_created": "20-12-2024", "issue_date": "22-12-2024"},
        {"username": "3", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "07-01-2025", "issue_date": "30-12-2024"},
        {"username": "4", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "11-12-2025", "issue_date": "30-12-2024"},
        {"username": "5", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "13-12-2024", "issue_date": "30-12-2024"},
        {"username": "6", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "12-02-2025", "issue_date": "30-12-2024"},
        {"username": "7", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "16-12-2024", "issue_date": "14-12-2024"},
        {"username": "8", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "15-12-2025", "issue_date": "25-12-2024"},
        {"username": "9", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "22-02-2025", "issue_date": "12-12-2024"},
        {"username": "10", "title": "учеба", "content": "подготовиться к экзамену", "date_created": "20-01-2025", "issue_date": "22-12-2024"},
    ]
        
display_notes(notes=notes, puge_number=1)