import csv
from collections import defaultdict

# Пример данных для записи в CSV файл
data = [
    ['№ заказа', 'Дата заказа', 'Название товара', 'Категория товара', 'Количество продаж', 'Цена за единицу', 'Общая стоимость'],

    [1, '01.04.2024', 'Рис', 'Крупы', 5, 115, 575],
    [2, '02.04.2024', 'Лимонад', 'Напитки', 7, 100, 700],
    [3, '03.04.2024', 'Стейк', 'Мясные продукты', 6, 550, 3300],
    [4, '04.04.2024', 'Йогурт', 'Молочные продукты', 4, 90, 360],
    [5, '05.04.2024', 'Редиска', 'Овощи', 3, 70, 210],
    [6, '06.04.2024', 'Груши', 'Фрукты', 7, 80, 560],
    [7, '07.04.2024', 'Квас', 'Напитки', 4, 130, 520],
    [8, '08.04.2024', 'Сок', 'Напитки', 6, 110, 660],
    [9, '09.04.2024', 'Конфеты', 'Сладости', 12, 75, 900],
    [10, '10.04.2024', 'Печенье', 'Сладости', 9, 95, 855]
]

# Запись данных в CSV файл
with open('sales_data.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in data:
        writer.writerow(row)

# Функция для чтения данных из CSV файла
def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Пропускаем заголовок
        for row in reader:
            # Преобразуем числовые значения в int и float
            row[4] = int(row[4])  # Количество продаж
            row[5] = float(row[5])  # Цена за единицу
            row[6] = float(row[6])  # Общая стоимость
            sales_data.append(row)
    return sales_data

# Функция для расчета общей выручки
def calculate_total_revenue(sales_data):
    total_revenue = sum(item[6] for item in sales_data)
    return total_revenue

# Функция для нахождения товара, проданного наибольшее количество раз
def find_most_sold_product(sales_data):
    product_sales = defaultdict(int)
    for item in sales_data:
        product_sales[item[2]] += item[4]
    most_sold_product = max(product_sales, key=product_sales.get)
    return most_sold_product, product_sales[most_sold_product]

# Функция для нахождения товара, принёсшего наибольшую выручку
def find_highest_revenue_product(sales_data):
    product_revenue = defaultdict(float)
    for item in sales_data:
        product_revenue[item[2]] += item[6]
    highest_revenue_product = max(product_revenue, key=product_revenue.get)
    return highest_revenue_product, product_revenue[highest_revenue_product]

# Функция для составления отчета
def generate_report(sales_data):
    total_revenue = calculate_total_revenue(sales_data)
    product_sales = defaultdict(int)
    product_revenue = defaultdict(float)

    for item in sales_data:
        product_sales[item[2]] += item[4]
        product_revenue[item[2]] += item[6]

    report = {
        'total_revenue': total_revenue,
        'product_sales': product_sales,
        'product_revenue': product_revenue,
        'product_share': {product: (revenue / total_revenue) * 100 for product, revenue in product_revenue.items()}
    }

    return report

# Основная функция
def main():
    file_path = 'sales_data.csv'  # Замените на путь к вашему CSV файлу
    sales_data = read_sales_data(file_path)

    total_revenue = calculate_total_revenue(sales_data)
    most_sold_product, most_sold_quantity = find_most_sold_product(sales_data)
    highest_revenue_product, highest_revenue = find_highest_revenue_product(sales_data)
    report = generate_report(sales_data)

    print(f'Общая выручка магазина: {total_revenue:.2f} руб.')
    print(f'Товар, который был продан наибольшее количество раз: {most_sold_product} ({most_sold_quantity} шт.)')
    print(f'Товар, который принес наибольшую выручку: {highest_revenue_product} ({highest_revenue:.2f} руб.)')

    print('\nОтчет:')
    print(f'Общая выручка: {report["total_revenue"]:.2f} руб.')
    for product, quantity in report['product_sales'].items():
        print(f'{product}: Продано {quantity} шт., Выручка {report["product_revenue"][product]:.2f} руб., Доля {report["product_share"][product]:.2f}%')

if __name__ == '__main__':
    main()