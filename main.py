

class Dog:

    # color = "color"
    # doger = "dogs"
    def __init__(self, color, doger):
        self.color = color
        self.doger = doger

    def bite(self):
        print("arrr  >:(")


dog1 = Dog("brown", "чихухуа")
# dog1.color = "brown"
# dog1.doger = "чихухуа"
dog2 = Dog()
dog2.color = "black"
dog2.doger = "овчарка"
print(dog1.color)
print(dog1.doger)
dog1.bite()
print(dog2.color)
print(dog2.doger)
dog2.bite()





