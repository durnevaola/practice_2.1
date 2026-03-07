import json
import os

file = "library.json"

# Create file if it does not exist
if not os.path.exists(file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump([], f)

while True:
    # Read books from file at the start of each loop iteration
    with open(file, "r", encoding="utf-8") as f:
        books = json.load(f)

    print("\n1-Показать")
    print("2-Поиск")
    print("3-Добавить")
    print("4-Сменить статус (доступна/недоступна)")
    print("5-Удалить")
    print("6-Экспорт доступных в txt")
    print("e-Выход и сохранение")

    c = input("Выберите: ").lower()

    if c == "1":
        for b in books:
            print(b)

    elif c == "2":
        t = input("Введите название или автора: ").lower()
        found = False
        for b in books:
            if t in b["title"].lower() or t in b["author"].lower():
                print(b)
                found = True
        if not found:
            print("Книги не найдены.")

    elif c == "3":
        books.append({
            "id": len(books) + 1,
            "title": input("Название: "),
            "author": input("Автор: "),
            "year": input("Год: "),
            "available": True
        })
        print("Книга добавлена. Она будет сохранена при выходе (опция 'e').")

    elif c == "4":
        try:
            i = int(input("ID книги для смены статуса: "))
            found = False
            for b in books:
                if b["id"] == i:
                    b["available"] = not b["available"]
                    print(f"Статус книги с ID {i} изменен. Она будет сохранена при выходе (опция 'e').")
                    found = True
                    break
            if not found:
                print("Книга с таким ID не найдена.")
        except ValueError:
            print("Некорректный ввод ID.")

    elif c == "5":
        try:
            i = int(input("ID книги для удаления: "))
            initial_count = len(books)
            books = [b for b in books if b["id"] != i]
            if len(books) < initial_count:
                print(f"Книга с ID {i} удалена. Она будет сохранена при выходе (опция 'e').")
            else:
                print("Книга с таким ID не найдена.")
        except ValueError:
            print("Некорректный ввод ID.")

    elif c == "6":
        with open("available_books.txt", "w", encoding="utf-8") as f:
            for b in books:
                if b["available"]:
                    # Formatting the output for readability in the text file
                    f.write(f"Название: {b['title']}, Автор: {b['author']}, Год: {b['year']}\n")
        print("Доступные книги экспортированы в 'available_books.txt'.")

    elif c == "e":
        # Save all current changes to library.json before exiting
        with open(file, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=4)  # Indent for readability
        print("Данные сохранены. Выход из программы.")
        break  # Exit the while loop

    else:
        print("Неверный ввод. Попробуйте снова.")
