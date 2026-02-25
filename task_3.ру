import csv

def read_products():
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row: 
                    products.append([row[0], float(row[1]), int(row[2])])
    except FileNotFoundError:
        products = [['Яблоки', 100, 50],
                   ['Бананы', 80, 30],
                   ['Молоко', 120, 20],
                   ['Хлеб', 40, 100]]
        save_products(products)
    return products

def save_products(products):
    with open('products.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Цена', 'Количество'])
        writer.writerows(products)

def show_all(products):
    print("\n--- Все товары ---")
    print("Название\tЦена\tКоличество")
    print("-" * 30)
    for product in products:
        print(f"{product[0]}\t{product[1]}\t{product[2]}")

def add_product(products):
    print("\n--- Добавление товара ---")
    name = input("Название: ")
    price = float(input("Цена: "))
    quantity = int(input("Количество: "))
    products.append([name, price, quantity])
    print(f"Товар {name} добавлен!")
def search_product(products):
    print("\n--- Поиск товара ---")
    search = input("Введите название для поиска: ").lower()
    found = False
    for product in products:
        if search in product[0].lower():
            print(f"Найден: {product[0]} - {product[1]} руб. - {product[2]} шт.")
            found = True
    if not found:
        print("Товары не найдены")

def total_cost(products):
    print("\n--- Общая стоимость ---")
    total = 0
    for product in products:
        cost = product[1] * product[2]
        print(f"{product[0]}: {product[1]} × {product[2]} = {cost} руб.")
        total += cost
    print(f"ИТОГО: {total} руб.")

def main():
    products = read_products()
    
    while True:
        print("\n" + "="*30)
        print("МЕНЮ:")
        print("1. Показать все товары")
        print("2. Добавить товар")
        print("3. Найти товар")
        print("4. Общая стоимость")
        print("5. Выход")
        print("="*30)
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            show_all(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            search_product(products)
        elif choice == '4':
            total_cost(products)
        elif choice == '5':
            save_products(products)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор!")
if __name__ == "__main__":
    main()
