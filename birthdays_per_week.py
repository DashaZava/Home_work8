from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримати поточну дату
    current_date = datetime.now().date()
    
    # Знайти перший день тижня (понеділок)
    monday = current_date - timedelta(days=current_date.weekday())
    
    # Знайти дату через тиждень
    next_week = monday + timedelta(weeks=1)
    
    # Створити словник для збереження іменинників за днями тижня
    birthdays_by_day = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    
    # Перебрати користувачів і розподілити їх за днями тижня
    for user in users:
        birthday = user['birthday'].date()
        
        # Якщо день народження попадає на тиждень вперед, то додати користувача до відповідного дня
        if current_date <= birthday < next_week:
            day_name = birthday.strftime('%A')
            if day_name == 'Saturday' or day_name == 'Sunday':
                birthdays_by_day['Monday'].append(user['name'])
            else:
                birthdays_by_day[day_name].append(user['name'])
    
    # Вивести іменинників за днями тижня
    for day, names in birthdays_by_day.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад тестового списку користувачів
test_users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 28)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 29)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 30)},
    {'name': 'Jan', 'birthday': datetime(2023, 9, 2)},
]

# Виклик функції з тестовим списком користувачів
get_birthdays_per_week(test_users)
