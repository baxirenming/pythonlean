class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # define a private function
    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


robot1 = Robot("Wilson", 25, "Hawaii")
robot2 = Robot("Wilson", 25, "Hawaii")
dictionary = {robot2: "Garice"}
print(dictionary[robot1])  # 输出: Garice
# 你设定 dictionary = {r1: "Hello"}，并不是“设定了 r1 和 r2 的值”，而是：
# 你通过自定义 __eq__ 和 __hash__，告诉 Python：“r1 和 r2 虽然是不同的对象，但在字典中可以当成同一个 key 来处理”。
# 所以你用 r2 来访问字典时，也能成功获取到 "Hello"。这就是字典和哈希的设计目的。
