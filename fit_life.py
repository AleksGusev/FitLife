# Модуль для завершения программы при ошибках
import sys

# Стандарт для расчета 30 мл на кг
WATER_PER_KG = 30
# Количество миллилитров в одном литре
LITER_WATER = 1000


# 1. Знакомство
greeting = 'Добро пожаловать в FitLife!'
print(greeting)
user_name = input('Как тебя зовут?\n')


# 2. Сбор данных
try:
    user_age = int(input('Сколько тебе лет?\n'))
    user_weight = float(input('Какой твой вес в кг?\n'))
    user_height = float(input('Какой у тебя рост в метрах (например 1.75)?\n'))
except ValueError:
    print('Для ввода возраста, веса и роста используй числа.')
    sys.exit()


# 3. Логика расчетов
try:
    # Расчет индекса массы тела
    bmi = round(user_weight / (user_height ** 2), 1)
except ZeroDivisionError:
    print('Рост не может быть равен нулю.')
    sys.exit()

# Расчет нормы воды в день
water_needed = round((user_weight * WATER_PER_KG) / LITER_WATER, 2)


# 4. Вывод красивого результата
print(f'Привет, {user_name}! Я знаю, что тебе {user_age} лет! :)')
print(f'Твой Индекс Массы Тела равен: {bmi}.')
print(f'Твоя рекомендуемая норма воды в день составляет: {water_needed} л.')
print('Расчет окончен. Будьте здоровы!')
