class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError(f"Тип {name} должен быть str")

        if not isinstance(age, int):
            raise TypeError(f"Тип {age} должен быть int")

        if age < 0 or age > 125:
            raise ValueError(f"Возраст: {age}, должен быть в диапазоне [0, 125]")

        self.__name = name
        self.__age = age

    def __repr__(self):
        return f"({self.__name}, {self.__age})"
