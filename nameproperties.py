class Person:
    def __init__(self, name):
        self._name = name  # 通常约定用 "_" 表示"私有"

    @property
    def name(self):
        return self._name  # getter

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("名字必须是字符串")
        self._name = value  # setter


p = Person("Eric")
print(p.name)     # 相当于 p.getName()
p.name = "Anna"   # 相当于 p.setName("Anna")
print(p.name)
