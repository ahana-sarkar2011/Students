class student():
    def __init__(self,sname,sage,slunch,sfavcolour,spassword):
        self.sname = sname
        self.sage = sage
        self.slunch = slunch
        self.sfavcolour = sfavcolour
        self.spassword = spassword
    def details(self):
        print("name: "+self.sname)
        print("age: "+str(self.sage))
        print("lunch: "+self.slunch)
        print("favourite colour: "+self.sfavcolour)
    def change_age(self):
        newage=int(input("how old are you now?"))
        self.sage = newage
    def login(self):
        attempt=input("Please type your password: ")
        if attempt == self.spassword:
            print("correct")
        else:
            print("incorrect")

s1 = student("Ahana",14,"yes", "pink","1p34m")
s2 = student("Lily",13,"no", "blue","56h4i")
s3 = student("Amelia",18,"no","red","s9ja5")

print(s1.sname)
print(s2.sage)
s2.details()
s1.change_age()
s1.details()
s3.login()