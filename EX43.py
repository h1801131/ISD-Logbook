class Student():
    def __init__(self, surname, lastname, studentnumber, course):
        self.surname = surname
        self.lastname = lastname
        self.studentnumber = studentnumber
        self.course = course
    def printDetails(self):
        print("Surname = ", self.surname)
        print("Lastname = ", self.lastname)
        print("Studentnumber = ", self.studentnumber)
        print("Course = ", self.course)
    def getSurname(self):
        return self.surname
    def getLastname(self):
        return self.lastname
    def getStudentnumber(self):
        return self.studentnumber
    def getCourse(self):
        return self.course
    def setSurname(self, surnameinput):
        self.surname = surnameinput
    def setLastname(self, lastnaminput):
        self.lastname = lastnameinput
    def setStudentnumber(self, studentnumberinput):
        self.studentnumber = studentnumberinput
    def setCourse(self, courseinput):
        self.course = courseinput
        
student1=Student("Ciuta" , "Costy",1234,"IT")
student1.printDetails()

student1=Student("Ciuta" , "Mary",1234,"IT")
student1.printDetails()




          
