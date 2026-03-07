def calculate_average(grades):
    return sum(grades) / len(grades)


try:
    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("Файл students.txt пуст.")
        exit()

    best_student = None
    best_average = 0
    passed_students = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        try:
            name, grades_str = line.split(":")
            grades = list(map(int, grades_str.split(",")))

            avg = calculate_average(grades)

            if avg > 4.0:
                passed_students.append(f"{name}:{avg:.2f}")

            if avg > best_average:
                best_average = avg
                best_student = name

        except ValueError:
            print(f"Ошибка в строке: {line}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

    with open("result.txt", "w", encoding="utf-8") as result_file:
        for student in passed_students:
            result_file.write(student + "\n")

    if best_student:
        print(f"Студент с наивысшим средним баллом: {best_student} ({best_average:.2f})")
    else:
        print("Не удалось определить лучшего студента.")

    print("Результаты записаны в result.txt")

except FileNotFoundError:
    print("Файл students.txt не найден. Проверь, что он лежит в той же папке.")
except Exception as e:
    print(f"Критическая ошибка: {e}")
