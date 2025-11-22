class student():
    def __init__(self,sname,sage):
        self.sname = sname
        self.sage = sage
    def details(self):
        print("name: "+self.sname)
        print("age: "+str(self.sage))

s1 = student("Ahana",14)
s2 = student("Lily",13)

print(s1.sname)
print(s2.sage)
s2.details()