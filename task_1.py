with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Я люблю программировать\n')
    f.write('Сегодня хорошая погода\n')
    f.write('Python это просто\n')
    f.write('Учусь работать с файлами\n')
    f.write('Задача выполнена успешно\n')

with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

print('Количество строк:', len(lines))

words = 0
for line in lines:
    words += len(line.split())
print('Количество слов:', words)

longest = ''
for line in lines:
    if len(line) > len(longest):
        longest = line
print('Самая длинная строка:', longest)
