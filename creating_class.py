import math
class student:
    def __init__(self,fn,ln,gender,gpa):
        self.fn=fn
        self.ln=ln
        self.gender=gender
        self.gpa=gpa
    def setFn(self,fn):
        self.fn=fn
    def getFn(self):
        return self.fn
    def setLn(self,ln):
        self.ln=ln
    def getLn(self):
        return self.ln
    def setGender(self,gender):
        self.gender=gender
    def getGender(self):
        return self.gender
    def setGpa(self,gpa):
        self.gpa=gpa
    def get_fn(self):
        return self.gpa
    def showMySelf(self):
        print(f"my First name is {self.fn}")
        print(f"my last name is {self.ln}")
        print(f"my gender is {self.gender}")
        print(f"my GPA is {self.gpa}")
    def studyTime(self,studyTime):
        self.gpa=self.gpa+math.log(studyTime)
        print(self.gpa)
Mahmoud=student("Mahmoud","Ahmed","Male",3.4)
Mahmoud.showMySelf()
Mahmoud.studyTime(10)
