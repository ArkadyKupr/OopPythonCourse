from pickle_task.person import Person
import pickle

persons_list = [Person("Андрей", 40),
                Person("Ирина", 41),
                Person("Андрей", 42),
                Person("Матфей", 45)]

with open("pickle_file", "wb") as file:
    pickle.dump(persons_list, file)
