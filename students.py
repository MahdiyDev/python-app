class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getInfo(self):
        return "Your name is " + str(self.name) + "! You are " + str(self.age) + " years old"
