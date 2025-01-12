name = 'Илья'
title = 'Покупка продуктов'
content = 'Молоко, яйца, соль, помидоры'
status = 'В процессе'
created_date = '01.01.2025'
issue_date = '02.01.2025'
temp_created_date = created_date[:-5]
temp_issue_date = issue_date[:-5]
print('Имя: ', name)
print('Покупка продуктов: ', title)
print('Список продуктов: ', content)
print('Статус: ', status)
print('Дата создания заметки: ', temp_created_date)
print('Дата истечения заметки: ', temp_issue_date)