class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError(f"Тип {name} должен быть str")

        if not isinstance(age, int):
            raise TypeError(f"Тип age: {age}, должен быть int")

        if age < 0:
            raise ValueError(f"Возраст age: {age}, должен быть >= 0")

        self.__name = name
        self.__age = age

    def __repr__(self):
        return f"{{{self.__name}: {self.__age}}}"
