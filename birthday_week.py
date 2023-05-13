import datetime

def get_birthdays_per_week(users):
    # Получаем текущую дату и время
    today = datetime.datetime.now()

    # Определяем дату на следующий понедельник
    next_monday = today + datetime.timedelta(days=(7 - today.weekday()))

    # Определяем дату на следующий воскресенье
    next_sunday = next_monday + datetime.timedelta(days=6)

    # Определяем дату на два дня назад
    two_days_ago = today - datetime.timedelta(days=2)

    # Создаем словарь, в котором ключами будут дни недели
    # а значениями - список именинников в этот день
    birthdays = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }

    # Итерируемся по списку пользователей
    for user in users:
        name = user['name']
        birthday = user['birthday']

        # Проверяем, находится ли день рождения в текущей неделе
        if next_monday <= birthday <= next_sunday or two_days_ago <= birthday < next_monday:
            # Определяем день недели дня рождения
            weekday = birthday.strftime('%A')

            # Добавляем имя пользователя в список именинников этого дня
            birthdays[weekday].append(name)

    # Выводим список именинников по дням недели
    for weekday, names in birthdays.items():
        if names:
            print(f'{weekday}: {", ".join(names)}')
