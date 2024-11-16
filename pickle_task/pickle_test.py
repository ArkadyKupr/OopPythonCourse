from pickle_task.person import Person
import pickle

persons_string = [Person("Андрей", 40),
                  Person("Ирина", 41),
                  Person("Андрей", 42),
                  Person("Матфей", 45)]

with open("pickle_file.txt", "wb") as file:
    pickle.dump(persons_string, file)

with open("pickle_file.txt", "rb") as file:
    persons_list_copy = pickle.load(file)

print(persons_string)
print(persons_list_copy)

print("Проверка, что получился такой же список:", str(persons_string) == str(persons_list_copy))
print("Проверка, что один и тот же объект:", persons_string is persons_list_copy)
