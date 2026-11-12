# Убрал импорт sys, так как больше не требуется
# Стандарт для расчета 30 мл на кг
WATER_PER_KG = 30
# Количество миллилитров в одном литре
LITER_WATER = 1000


# 1. Знакомство
greeting = 'Добро пожаловать в FitLife!'
print(greeting)
user_name = input('Как тебя зовут?\n')


# 2. Сбор данных
# Цикл while для определения возраста
while True:
    # Вынес переменную с запросом за конструкцию try/except, чтобы использовать введенное пользователем значение в except
    raw_user_age = input('Сколько тебе лет?\n')
    try:
        user_age = int(raw_user_age)
        break
    except ValueError:
        print(f'Некорректное значение возраста - {raw_user_age}. Используй цифры.')

# Цикл while для определения веса
while True:
    raw_user_weight = input('Какой твой вес в кг?\n')
    try:
        user_weight = float(raw_user_weight)
        break
    except ValueError:
        print(f'Некорректное значение веса - {raw_user_weight}. Введи вес цифрами (например 80.5).')

# Цикл while для определения роста
while True:
    raw_user_height = input('Какой у тебя рост в метрах?\n')
    try:
        user_height = float(raw_user_height)
        # Логическое выражение с if заменит try/except из шага 3
        if user_height <= 0:
            print('Рост не может быть равен нулю.')
            continue
        break
    except ValueError:
        print(f'Некорректное значение роста - {raw_user_height}. Введи рост цифрами (например 1.75).')


# 3. Логика расчетов
# Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды в день
water_needed = round((user_weight * WATER_PER_KG) / LITER_WATER, 2)


# 4. Вывод красивого результата
print(f'Привет, {user_name}! Я знаю, что тебе {user_age} лет! :)')
print(f'Твой Индекс Массы Тела равен: {bmi}.')
print(f'Твоя рекомендуемая норма воды в день составляет: {water_needed} л.')
print('Расчет окончен. Будьте здоровы!')
