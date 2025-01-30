class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def increaseAge(self):
        self.age += 1

    def decrease(self):
        if self.age > 0:
            self.age -= 1

    def __str__(self):
        return f"{self.name} is {self.age} years old"

David = MyClass("David",6)
David.decrease()
David.decrease()


