from students import Students


class People(Students):
    def __init__(self, name, age, phoneNumber):
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber
    def getInfo(self):
        return "Your name is " + str(self.name) + "! You are " + str(self.age) + " years old. Your phone number is " + str(self.phoneNumber)