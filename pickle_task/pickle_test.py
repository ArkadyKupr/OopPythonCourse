from pickle_task.person import Person
import pickle

persons_list = list([Person("Андрей", 40),
                     Person("Ирина", 41),
                     Person("Андрей", 42),
                     Person("Матфей", 45)])

with open("pickle_file.txt", "wb") as file:
    pickle.dump(persons_list, file)

with open("pickle_file.txt", "rb") as file:
    persons_list_copy = pickle.load(file)

print(persons_list)
print(persons_list_copy)

print(persons_list == persons_list_copy)
print(persons_list is persons_list_copy)
