class User:
    def __init__(self,_id ,username, pwd):
        self._id = _id
        self.username = username
        self.password = pwd
    def login (self,uname,pwd):
        if self.username == uname and self.password == pwd:
            return "login sucessful"
        return "Unathorised User"

class Teacher(User):
    def __init__(self, _id, username, pwd , designation):
        super().__init__(_id, username, pwd)
        self.designation = designation

class Student(User):
    def __init__(self, _id,username,pwd, faculty):
        super().__init__(_id,username, pwd)
        self.faculty = faculty

t = Teacher(1,"teacher","teacher","professor")
s = Student(2,"student","student","BCT")
uname = input("Enter Username:")
pwd = input("Enter Password:")
#print(t.login(uname,pwd))
print(s.login(uname,pwd))