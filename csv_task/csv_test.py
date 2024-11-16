from csv_task.person import Person
import csv

persons = [Person("Андрей", 40),
           Person("Ирина", 41),
           Person("Андрей", 42),
           Person("Матфей", 45)]

persons_copy = []

with open("file.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    for person in persons:
        writer.writerow([person.name, person.age])

with open("file.csv", "r", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        persons_copy.append(row)

print(persons)
print(persons_copy)

print("Проверка, что получился такой же список:", str(persons) == str(persons_copy))
print("Проверка, что один и тот же объект:", persons is persons_copy)
