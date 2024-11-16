from json_task.person import Person
import json


def serialize_user(obj):
    if isinstance(obj, Person):
        return obj.__dict__

    raise TypeError(f"Unexpected type: {obj.__class__.__name__}")


def deserialize_user(dct):
    return Person(dct["name"], dct["age"])


persons = [Person("Андрей", 40),
           Person("Ирина", 41),
           Person("Андрей", 42),
           Person("Матфей", 45)]

with open("json_file.json", "w") as file:
    json.dump(persons, file, default=serialize_user)

with open("json_file.json", "r") as file:
    persons_copy = json.load(file, object_hook=deserialize_user)

print(persons)
print(persons_copy)

print("Проверка, что получился такой же список:", persons == persons_copy)
print("Проверка, что один и тот же объект:", persons is persons_copy)
