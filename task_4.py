import datetime

LOG_FILE = 'calculator.log'

def show_last_operations():
    """Показать последние 5 операций"""
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                print("\n--- Последние 5 операций ---")
                for line in lines[-5:]:
                    print(line.strip())
            else:
                print("\nИстория операций пуста")
    except FileNotFoundError:
        print("\nИстория операций пока пуста")

def log_operation(text):
    """Записать операцию в файл"""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def clear_log():
    """Очистить лог-файл"""
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write('')
    print("Лог-файл очищен!")

show_last_operations()

while True:
    print("\n" + "="*30)
    print("Калькулятор")
    print("1. Посчитать")
    print("2. Очистить историю")
    print("3. Выход")
    
    choice = input("Выберите действие: ")
     if choice == '1':
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            op = input("Введите операцию (+, -, *, /): ")
            
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a / b
            else:
                print("Неверная операция!")
                continue
            
            print(f"Результат: {result}")
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_text = f"[{timestamp}] {a} {op} {b} = {result}"
            log_operation(log_text)
            
        except ValueError:
            print("Ошибка: введите числа!")
    
    elif choice == '2':
        confirm = input("Точно очистить историю? (да/нет): ")
        if confirm.lower() == 'да':
            clear_log()
    
    elif choice == '3':
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор!")
