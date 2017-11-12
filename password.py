class User():
    def __init__(self, name):
        self.name = name
        self.__password = "pass"
    def setPassword(self, password):
        self.__password = password
    def getPassword(self):
        return self.__password


arek = User("Arek")
print(arek.getPassword())
