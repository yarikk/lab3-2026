# ============================= УВАГА! =============================
# Цей файл містить ПРИКЛАД виконання лабораторної роботи.
# Ваше завдання - розробити ВЛАСНУ програму згідно з вашим варіантом.
#
# Ви можете використовувати цей код як зразок, але не копіювати його.
# Повністю замініть цей код своєю реалізацією.
#
# Ваш код повинен відповідати таким вимогам:
# 1. Обрана предметна область згідно з вашим варіантом.
# 2. Реалізовано всі необхідні функції:
#    - додавання, видалення, оновлення даних
#    - пошук та фільтрація
#    - обчислення статистик (середнє, min/max)
#    - групування та агрегація
# 3. Використано map(), filter(), reduce(), сортування, зрізи.
# 4. Реалізовано операції з множинами та словниками.
# 5. Створено інтерактивне меню для користувача.
# =================================================================

from collections import defaultdict
from functools import reduce
import datetime

# Підготовка даних (Список словників для системи бронювання готелів)
bookings_data = [
    {"id": 1, "guest": "Олександр Петренко", "room_number": 101, "room_type": "Single", "price": 1000, "nights": 3, "check_in": "2026-06-01"},
    {"id": 2, "guest": "Марія Іваненко", "room_number": 202, "room_type": "Double", "price": 1800, "nights": 5, "check_in": "2026-06-02"},
    {"id": 3, "guest": "Іван Коваль", "room_number": 305, "room_type": "Suite", "price": 3500, "nights": 2, "check_in": "2026-06-05"},
    {"id": 4, "guest": "Олена Шевченко", "room_number": 102, "room_type": "Single", "price": 1000, "nights": 4, "check_in": "2026-06-03"},
    {"id": 5, "guest": "Андрій Мельник", "room_number": 203, "room_type": "Double", "price": 1800, "nights": 1, "check_in": "2026-06-04"},
]

# Список усіх наявних номерів у готелі (для роботи з множинами)
all_hotel_rooms = {101, 102, 103, 201, 202, 203, 301, 305}

# Базові операції зі структурами даних
def add_booking(data, booking):
    """Додає нове бронювання."""
    data.append(booking)
    print("Бронювання додано успішно.")

def remove_booking(data, index):
    """Видаляє бронювання за індексом."""
    if 0 <= index < len(data):
        del data[index]
        print("Бронювання видалено успішно.")
    else:
        print("Невірний індекс.")

def update_booking(data, index, key, value):
    """Оновлює інформацію про бронювання."""
    if 0 <= index < len(data):
        if key in ['id', 'room_number', 'price', 'nights']:
            try:
                value = int(value) if key != 'price' else float(value)
            except ValueError:
                print(f"Невірний тип значення для ключа '{key}'")
                return
        data[index][key] = value
        print("Інформацію оновлено успішно.")
    else:
        print("Невірний індекс.")

def find_bookings_by_guest(data, guest_name):
    """Знаходить бронювання за ім'ям гостя (використання filter)."""
    return list(filter(lambda x: guest_name.lower() in x["guest"].lower(), data))

# Специфічні функції аналізу
def calculate_total_revenue(data):
    """Обчислює загальний дохід за допомогою reduce та map."""
    costs = list(map(lambda x: x["price"] * x["nights"], data))
    return reduce(lambda acc, cost: acc + cost, costs, 0)

def calculate_statistics(data):
    """Обчислює середнє, мінімальне та максимальне значення тривалості проживання."""
    if not data:
        return 0, 0, 0
    nights_list = [b["nights"] for b in data]
    avg_nights = sum(nights_list) / len(nights_list)
    min_nights = min(nights_list)
    max_nights = max(nights_list)
    return avg_nights, min_nights, max_nights

# Вбудовані функції, сортування та зрізи
def sort_bookings_by_date(data):
    """Сортує бронювання за датою заїзду."""
    return sorted(data, key=lambda x: datetime.datetime.strptime(x["check_in"], "%Y-%m-%d"))

def get_top_bookings(data, n=3):
    """Повертає топ-N найдорожчих бронювань (використання зрізів)."""
    sorted_by_cost = sorted(data, key=lambda x: x["price"] * x["nights"], reverse=True)
    return sorted_by_cost[:n]

# Робота з множинами та словниками
def analyze_room_occupancy(data):
    """Демонстрація операцій з множинами: зайняті та вільні номери."""
    booked_rooms = {b["room_number"] for b in data}
    
    # Перетин: заброньовані номери, які є в готелі
    active_booked = booked_rooms.intersection(all_hotel_rooms)
    
    # Різниця: вільні номери (які є в готелі, але не заброньовані)
    free_rooms = all_hotel_rooms.difference(booked_rooms)
    
    print(f"\nЗаброньовані номери: {active_booked}")
    print(f"Вільні номери: {free_rooms}")

def group_bookings_by_type(data):
    """Групує бронювання за типом номеру (використання defaultdict)."""
    grouped = defaultdict(list)
    for booking in data:
        grouped[booking["room_type"]].append(booking)
    return dict(grouped)

# Інтерактивне меню
def print_menu():
    """Виводить меню опцій."""
    print("\n==== Система бронювання готелів ====")
    print("1. Показати всі бронювання")
    print("2. Додати нове бронювання")
    print("3. Видалити бронювання")
    print("4. Оновити інформацію про бронювання")
    print("5. Знайти бронювання за ім'ям гостя")
    print("6. Обчислити загальний дохід готелю")
    print("7. Статистика проживання (середнє, min, max ночей)")
    print("8. Групувати бронювання за типом номеру")
    print("9. Сортувати бронювання за датою заїзду")
    print("10. Показати топ найдорожчих бронювань (зрізи)")
    print("11. Аналіз занять номерів (множини)")
    print("0. Вийти")

def main():
    """Головна функція програми."""
    global bookings_data
    while True:
        print_menu()
        choice = input("Оберіть опцію: ")

        if choice == "1":
            if not bookings_data:
                print("Немає даних про бронювання.")
            for i, b in enumerate(bookings_data):
                print(f"[{i}] {b}")
        elif choice == "2":
            try:
                b_id = int(input("Введіть ID бронювання: "))
                guest = input("Введіть ПІБ гостя: ")
                room_number = int(input("Введіть номер кімнати: "))
                room_type = input("Введіть тип номеру (Single/Double/Suite): ")
                price = float(input("Введіть ціну за ніч: "))
                nights = int(input("Введіть кількість ночей: "))
                check_in = input("Введіть дату заїзду (YYYY-MM-DD): ")
                datetime.datetime.strptime(check_in, "%Y-%m-%d") # перевірка формату дати
                
                new_booking = {
                    "id": b_id, "guest": guest, "room_number": room_number,
                    "room_type": room_type, "price": price, "nights": nights, "check_in": check_in
                }
                add_booking(bookings_data, new_booking)
            except ValueError:
                print("Помилка введення даних. Перевірте числові поля та формат дати.")
        elif choice == "3":
            try:
                index = int(input("Введіть індекс бронювання для видалення: "))
                remove_booking(bookings_data, index)
            except ValueError:
                print("Невірний індекс. Введіть число.")
        elif choice == "4":
            try:
                index = int(input("Введіть індекс для оновлення: "))
                if not (0 <= index < len(bookings_data)):
                    print("Невірний індекс.")
                    continue
                key = input("Введіть ключ для оновлення (id/guest/room_number/room_type/price/nights/check_in): ")
                if key not in bookings_data[0]:
                    print("Невірний ключ.")
                    continue
                value = input("Введіть нове значення: ")
                update_booking(bookings_data, index, key, value)
            except ValueError:
                print("Невірний індекс.")
        elif choice == "5":
            name = input("Введіть ім'я гостя для пошуку: ")
            results = find_bookings_by_guest(bookings_data, name)
            if results:
                for r in results:
                    print(r)
            else:
                print("Нічого не знайдено.")
        elif choice == "6":
            total = calculate_total_revenue(bookings_data)
            print(f"Загальний дохід готелю: {total} грн")
        elif choice == "7":
            avg, min_n, max_n = calculate_statistics(bookings_data)
            print(f"Статистика ночей: Середнє = {avg:.2f}, Мінімум = {min_n}, Максимум = {max_n}")
        elif choice == "8":
            grouped = group_bookings_by_type(bookings_data)
            for r_type, items in grouped.items():
                print(f"\nТип номеру: {r_type}")
                for item in items:
                    print(f"  {item}")
        elif choice == "9":
            sorted_b = sort_bookings_by_date(bookings_data)
            print("\nБронювання за датою заїзду:")
            for b in sorted_b:
                print(b)
        elif choice == "10":
            top = get_top_bookings(bookings_data, 2)
            print("\nТоп найдорожчих бронювань:")
            for b in top:
                print(b)
        elif choice == "11":
            analyze_room_occupancy(bookings_data)
        elif choice == "0":
            print("Дякуємо за використання програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()